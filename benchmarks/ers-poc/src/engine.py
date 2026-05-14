import json
import time
from pathlib import Path
from typing import Iterator, List, Optional, Tuple, Dict

from datasets import load_dataset
from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCase, LLMTestCaseParams
from litellm import completion
from tenacity import retry, stop_after_attempt, wait_exponential

from .config import HF_DATASET_PATH, PATHS, LOCAL_DATASET_PATH
from .models import EvaluationItem, GenerationItem, QuestionRecord
from .prompts import CANDIDATE_SYSTEM_PROMPT, JUDGE_CRITERIA

# ==========================================
# ORCHESTRATORS
# ==========================================

# Orchestrators placed at the top are both the module map and its summary

def execute_generation(model_id: str, limit: Optional[int] = None) -> None:
    records = fetch_dataset(limit)
    generations = fetch_generations(model_id)

    pending_tasks = filter_pending_generation_tasks(records, generations)

    for record, context_type, context_text in pending_tasks:
        new_generation = generate_single_answer(model_id, record, context_type, context_text)
        generations.append(new_generation)
        persist_generations(model_id, generations)

def execute_evaluation(
    model_id: str, limit: Optional[int] = None, judge_model: Optional[str] = None
) -> None:
    records = fetch_dataset(limit)
    generations = fetch_generations(model_id)

    if not generations:
        print(f"No generations found for {model_id}. Skipping evaluation.")
        return

    judge_name = judge_model or "deepeval_default"
    evaluations = fetch_evaluations(model_id, judge_name)

    pending_tasks = filter_pending_evaluation_tasks(records, generations, evaluations)
    metric = build_evaluation_metric(judge_name)

    for record, generation in pending_tasks:
        new_evaluation = evaluate_single_answer(metric, record, generation, judge_name)
        evaluations.append(new_evaluation)
        persist_evaluations(model_id, judge_name, evaluations)

# ==========================================
# MECHANISMS
# ==========================================

def filter_pending_generation_tasks(
    records: List[QuestionRecord], existing_generations: List[GenerationItem]
) -> List[Tuple[QuestionRecord, str, str]]:
    
    valid_generations = [
        g for g in existing_generations 
        if not (
            g.actual_output.startswith("ERROR:") or 
            g.finish_reason in ("length", "content_filter", "error")
        )
    ]

    processed_keys = {
        (g.domain, g.sample_id, g.question_id, g.context_type) for g in valid_generations
    }
    
    pending_tasks = []
    for record in records:
        if (record.domain, record.sample_id, record.question_id, "source") not in processed_keys:
            pending_tasks.append((record, "source", record.source))
        if (record.domain, record.sample_id, record.question_id, "ers") not in processed_keys:
            pending_tasks.append((record, "ers", record.ers_artifact))
            
    return pending_tasks

def generate_single_answer(
    model_id: str, record: QuestionRecord, context_type: str, context_text: str
) -> GenerationItem:
    try:
        output, finish_reason, latency_ms, prompt_tokens, completion_tokens, cost = request_llm_completion(model_id, context_text, record.question)
    except Exception as e:
        print(f"Network error during generation for model {model_id}: {e}")
        output, finish_reason, latency_ms, prompt_tokens, completion_tokens, cost = f"ERROR: {str(e)}", "error", 0.0, 0, 0, 0.0

    return GenerationItem(
        domain=record.domain,
        sample_id=record.sample_id,
        question_id=record.question_id,
        context_type=context_type,
        question=record.question,
        expected_answer=record.answer,
        actual_output=output,
        finish_reason=finish_reason,
        latency_ms=latency_ms,
        prompt_tokens=prompt_tokens,
        completion_tokens=completion_tokens,
        cost=cost,
        model_id=model_id
    )

def filter_pending_evaluation_tasks(
    records: List[QuestionRecord],
    generations: List[GenerationItem],
    existing_evaluations: List[EvaluationItem]
) -> List[Tuple[QuestionRecord, GenerationItem]]:
    
    record_map = {(r.domain, r.sample_id, r.question_id): r for r in records}
    
    valid_generation_keys = {
        (g.domain, g.sample_id, g.question_id, g.context_type) for g in generations
    }
    
    valid_evaluations = [
        e for e in existing_evaluations 
        if not e.reason.startswith("ERROR:") and 
           (e.domain, e.sample_id, e.question_id, e.context_type) in valid_generation_keys
    ]
    
    processed_keys = {
        (e.domain, e.sample_id, e.question_id, e.context_type) for e in valid_evaluations
    }

    pending_tasks = []
    for generation in generations:
        if (generation.domain, generation.sample_id, generation.question_id, generation.context_type) in processed_keys:
            continue

        key = (generation.domain, generation.sample_id, generation.question_id)
        record = record_map.get(key)
        if record:
            pending_tasks.append((record, generation))
            
    return pending_tasks

def build_evaluation_metric(model_name: str) -> GEval:
    return GEval(
        name="Reasoning Integrity",
        criteria=JUDGE_CRITERIA,
        evaluation_params=[
            LLMTestCaseParams.INPUT,
            LLMTestCaseParams.ACTUAL_OUTPUT,
            LLMTestCaseParams.EXPECTED_OUTPUT,
        ],
        strict_mode=False,
        model=model_name
    )

def evaluate_single_answer(
    metric: GEval, record: QuestionRecord, generation: GenerationItem, judge_model: str
) -> EvaluationItem:
    try:
        test_case = LLMTestCase(
            input=record.question,
            actual_output=generation.actual_output,
            expected_output=record.answer,
        )
        metric.measure(test_case)
        score = metric.score
        reason = metric.reason
    except Exception as e:
        print(f"Network error during evaluation: {e}")
        score = 0.0
        reason = f"ERROR: {str(e)}"

    return EvaluationItem(
        domain=generation.domain,
        sample_id=generation.sample_id,
        question_id=generation.question_id,
        context_type=generation.context_type,
        score=score,
        reason=reason,
        candidate_id=generation.model_id,
        judge_id=judge_model
    )

@retry(wait=wait_exponential(multiplier=1, min=4, max=10), stop=stop_after_attempt(3))
def request_llm_completion(
    model_id: str, context: str, question: str
) -> Tuple[str, str, float, int, int, float]:
    messages = [
        {"role": "system", "content": CANDIDATE_SYSTEM_PROMPT},
        {"role": "user", "content": f"<START_CONTEXT>\n{context}\n<END_CONTEXT>\n\n<START_QUESTION>\n{question}\n<END_QUESTION>"},
    ]
    start_time = time.time()
    response = completion(model=model_id, messages=messages)
    end_time = time.time()

    actual_output = response.choices[0].message.content
    finish_reason = response.choices[0].finish_reason or "unknown"
    latency_ms = (end_time - start_time) * 1000

    prompt_tokens = getattr(response.usage, 'prompt_tokens', 0) if hasattr(response, 'usage') and response.usage else 0
    completion_tokens = getattr(response.usage, 'completion_tokens', 0) if hasattr(response, 'usage') and response.usage else 0
    cost = getattr(response.usage, 'cost', 0.0) if hasattr(response, 'usage') and response.usage else 0.0

    return actual_output, finish_reason, latency_ms, prompt_tokens, completion_tokens, cost

def fetch_dataset(limit: Optional[int] = None) -> List[QuestionRecord]:
    if not LOCAL_DATASET_PATH.exists():
        download_hf_dataset()
    return read_local_dataset(limit)

def download_hf_dataset() -> None:
    print(f"Dataset not found at {LOCAL_DATASET_PATH}. Downloading from HF...")
    LOCAL_DATASET_PATH.parent.mkdir(parents=True, exist_ok=True)
    dataset = load_dataset(HF_DATASET_PATH, split="test")
    dataset.to_json(str(LOCAL_DATASET_PATH))

def read_local_dataset(limit: Optional[int] = None) -> List[QuestionRecord]:
    records = []
    with open(LOCAL_DATASET_PATH, "r", encoding="utf-8") as f:
        for line in f:
            records.append(QuestionRecord(**json.loads(line)))

    if limit is not None:
        return records[:limit]
    return records

def fetch_generations(model_id: str) -> List[GenerationItem]:
    path = get_candidate_path(model_id)
    if not path.exists():
        return []
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [GenerationItem(**item) for item in data]

def fetch_evaluations(model_id: str, judge_model: str) -> List[EvaluationItem]:
    path = get_evaluation_path(model_id, judge_model)
    if not path.exists():
        return []
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [EvaluationItem(**item) for item in data]

def fetch_all_evaluations(model_id: str) -> Dict[str, List[EvaluationItem]]:
    safe_name = sanitize_model_id(model_id)
    evaluations_by_judge = {}
    prefix = f"{safe_name}_"
    suffix = "_evaluations.json"
    
    if PATHS["EVALS_DIR"].exists():
        for path in PATHS["EVALS_DIR"].glob(f"{prefix}*{suffix}"):
            judge_safe = path.name[len(prefix):-len(suffix)]
            with open(path, "r", encoding="utf-8") as f:
                file_data = json.load(f)
            evaluations_by_judge[judge_safe] = [EvaluationItem(**item) for item in file_data]
            
    return evaluations_by_judge

def persist_generations(model_id: str, generations: List[GenerationItem]) -> None:
    ensure_dirs()
    path = get_candidate_path(model_id)
    tmp_path = path.with_suffix(".tmp")

    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump([g.model_dump() for g in generations], f, indent=2)

    tmp_path.replace(path)

def persist_evaluations(model_id: str, judge_model: str, evaluations: List[EvaluationItem]) -> None:
    ensure_dirs()
    path = get_evaluation_path(model_id, judge_model)
    tmp_path = path.with_suffix(".tmp")

    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump([e.model_dump() for e in evaluations], f, indent=2)

    tmp_path.replace(path)

def sanitize_model_id(model_id: str) -> str:
    return model_id.replace("/", "_", -1).replace(":", "_", -1)

def get_candidate_path(model_id: str) -> Path:
    safe_name = sanitize_model_id(model_id)
    return PATHS["CANDIDATES_DIR"] / f"{safe_name}_candidate.json"

def get_evaluation_path(model_id: str, judge_model: str) -> Path:
    safe_name = sanitize_model_id(model_id)
    safe_judge = sanitize_model_id(judge_model)
    return PATHS["EVALS_DIR"] / f"{safe_name}_{safe_judge}_evaluations.json"

def ensure_dirs() -> None:
    PATHS["CANDIDATES_DIR"].mkdir(parents=True, exist_ok=True)
    PATHS["EVALS_DIR"].mkdir(parents=True, exist_ok=True)
