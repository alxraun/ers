from typing import List, Dict, Tuple, Optional
from collections import defaultdict
from dataclasses import dataclass
import tiktoken
from .config import PATHS, TIKTOKEN_ENCODING
from .models import QuestionRecord, GenerationItem, EvaluationItem

PERCENTAGE_MULTIPLIER = 100.0
DEFAULT_SORT_WEIGHT = 99
CONTEXT_SOURCE = "source"
CONTEXT_ERS = "ers"
SCOPE_OVERALL = "overall"
SCOPE_AVERAGE = "avg"
KEY_GENERATIONS = "generations"
KEY_EVALUATIONS = "evaluations"
TYPE_SIMPLE = "simple"
TYPE_COMPLEX = "complex"

_ENCODER = tiktoken.get_encoding(TIKTOKEN_ENCODING)

@dataclass
class TokenMetrics:
    sample_count: int
    compression_ratio: float
    performance_retention: float
    score_delta: float
    average_source_tokens: float
    average_ers_tokens: float

@dataclass
class ScoreBreakdownRow:
    label: str
    source_score: float
    ers_score: float
    delta: float

@dataclass
class ModelEvaluationResult:
    candidate_id: str
    judge_id: str
    token_metrics: TokenMetrics
    score_breakdown: List[ScoreBreakdownRow]

class BenchmarkDataIndex:
    def __init__(self, records: List[QuestionRecord], generations: List[GenerationItem]):
        self.records = {
            (record.domain, record.sample_id, record.question_id): record 
            for record in records
        }
        self.generations = {
            (generation.domain, generation.sample_id, generation.question_id, generation.context_type): generation 
            for generation in generations
        }

    def get_record(self, evaluation: EvaluationItem) -> Optional[QuestionRecord]:
        return self.records.get((evaluation.domain, evaluation.sample_id, evaluation.question_id))

    def get_generation(self, evaluation: EvaluationItem) -> Optional[GenerationItem]:
        return self.generations.get((evaluation.domain, evaluation.sample_id, evaluation.question_id, evaluation.context_type))

def count_tokens(text: str) -> int:
    return len(_ENCODER.encode(text))

def calculate_average(values: List[float]) -> float:
    if not values:
        return 0.0
    return sum(values) / len(values)

def calculate_compression_ratio(source_tokens: int, ers_tokens: int) -> float:
    if source_tokens == 0:
        return 0.0
    return (1.0 - (ers_tokens / source_tokens)) * PERCENTAGE_MULTIPLIER

def calculate_performance_retention(source_score: float, ers_score: float) -> float:
    if source_score == 0.0:
        if ers_score == 0.0:
            return PERCENTAGE_MULTIPLIER
        return float('inf')
    return (ers_score / source_score) * PERCENTAGE_MULTIPLIER

def sort_by_question_type(question_type: str) -> int:
    sort_order = {TYPE_SIMPLE: 0, TYPE_COMPLEX: 1, SCOPE_AVERAGE: 2}
    return sort_order.get(question_type, DEFAULT_SORT_WEIGHT)

def resolve_participant_ids(evaluations: List[EvaluationItem], fallback_ids: Tuple[str, str]) -> Tuple[str, str]:
    fallback_candidate, fallback_judge = fallback_ids
    for evaluation in evaluations:
        if evaluation.candidate_id and evaluation.judge_id:
            return evaluation.candidate_id, evaluation.judge_id
    return fallback_candidate, fallback_judge

def calculate_token_metrics(evaluations: List[EvaluationItem], data_index: BenchmarkDataIndex) -> Optional[TokenMetrics]:
    sample_metrics = defaultdict(lambda: {"source_tokens": 0, "ers_tokens": 0, "source_score": 0.0, "ers_score": 0.0})
    
    for evaluation in evaluations:
        record = data_index.get_record(evaluation)
        generation = data_index.get_generation(evaluation)
        
        if not record or not generation:
            continue
            
        item_key = (evaluation.domain, evaluation.sample_id, evaluation.question_id)
        sample_metrics[item_key]["source_tokens"] = count_tokens(record.source)
        sample_metrics[item_key]["ers_tokens"] = count_tokens(record.ers_artifact)
        
        if evaluation.context_type == CONTEXT_SOURCE:
            sample_metrics[item_key]["source_score"] = evaluation.score
        else:
            sample_metrics[item_key]["ers_score"] = evaluation.score

    sample_count = len(sample_metrics)
    if sample_count == 0:
        return None

    total_source_tokens = sum(sample_metric["source_tokens"] for sample_metric in sample_metrics.values())
    total_ers_tokens = sum(sample_metric["ers_tokens"] for sample_metric in sample_metrics.values())
    average_source_score = calculate_average([sample_metric["source_score"] for sample_metric in sample_metrics.values()])
    average_ers_score = calculate_average([sample_metric["ers_score"] for sample_metric in sample_metrics.values()])
    
    return TokenMetrics(
        sample_count=sample_count,
        compression_ratio=calculate_compression_ratio(total_source_tokens, total_ers_tokens),
        performance_retention=calculate_performance_retention(average_source_score, average_ers_score),
        score_delta=average_ers_score - average_source_score,
        average_source_tokens=total_source_tokens / sample_count,
        average_ers_tokens=total_ers_tokens / sample_count
    )

def aggregate_domain_scores(evaluations: List[EvaluationItem], data_index: BenchmarkDataIndex) -> Dict[str, Dict[str, Dict[str, List[float]]]]:
    domain_scores = defaultdict(lambda: defaultdict(lambda: {CONTEXT_SOURCE: [], CONTEXT_ERS: []}))
    
    for evaluation in evaluations:
        record = data_index.get_record(evaluation)
        if not record:
            continue
        
        for scope in [record.domain, SCOPE_OVERALL]:
            domain_scores[scope][record.question_type][evaluation.context_type].append(evaluation.score)
            domain_scores[scope][SCOPE_AVERAGE][evaluation.context_type].append(evaluation.score)
            
    return domain_scores

def format_score_breakdown(domain_scores: Dict[str, Dict[str, Dict[str, List[float]]]]) -> List[ScoreBreakdownRow]:
    formatted_breakdown = []
    sorted_domains = [SCOPE_OVERALL] + sorted([domain for domain in domain_scores.keys() if domain != SCOPE_OVERALL])
    
    for domain in sorted_domains:
        if domain not in domain_scores:
            continue
        
        question_types = domain_scores[domain]
        sorted_question_types = sorted(question_types.keys(), key=sort_by_question_type)
        
        for question_type in sorted_question_types:
            scores = question_types[question_type]
            source_average = calculate_average(scores[CONTEXT_SOURCE])
            ers_average = calculate_average(scores[CONTEXT_ERS])
            
            formatted_breakdown.append(ScoreBreakdownRow(
                label=f"{domain}: {question_type}",
                source_score=source_average,
                ers_score=ers_average,
                delta=ers_average - source_average
            ))
            
    return formatted_breakdown

def collect_evaluation_summaries(records: List[QuestionRecord], benchmark_results: Dict[str, Dict[str, List]]) -> List[ModelEvaluationResult]:
    summaries = []
    
    for model_slug, model_data in sorted(benchmark_results.items()):
        generations = model_data.get(KEY_GENERATIONS, [])
        data_index = BenchmarkDataIndex(records, generations)
        evaluations_by_judge = model_data.get(KEY_EVALUATIONS, {})
        
        for judge_slug, evaluations in sorted(evaluations_by_judge.items()):
            token_metrics = calculate_token_metrics(evaluations, data_index)
            if not token_metrics:
                continue
                
            domain_scores = aggregate_domain_scores(evaluations, data_index)
            score_breakdown = format_score_breakdown(domain_scores)
            candidate_id, judge_id = resolve_participant_ids(evaluations, (model_slug, judge_slug))
            
            summaries.append(ModelEvaluationResult(
                candidate_id=candidate_id,
                judge_id=judge_id,
                token_metrics=token_metrics,
                score_breakdown=score_breakdown
            ))
            
    return summaries

def render_report_header() -> List[str]:
    return [
        "# ERS-PoC Benchmark Report",
        "",
        "> **Glossary:**",
        "> * **Compression Ratio (CR):** `(1.0 - (tokens_ers / tokens_source)) * 100.0`",
        "> * **Performance Retention (PR):** `(score_ers / score_source) * 100.0`",
        "> * **Score:** Average accuracy (0.0 to 1.0) awarded by the Judge based on answer correctness with Ground Truth.",
        "> * **Δ (Delta):** `score_ers - score_source`",
        "> * **Simple QA:** Direct fact retrieval.",
        "> * **Complex QA:** Multi-hop reasoning.",
        "\n---\n"
    ]

def sort_summaries_for_leaderboard(summaries: List[ModelEvaluationResult]) -> List[ModelEvaluationResult]:
    return sorted(
        summaries,
        key=lambda summary: (summary.token_metrics.performance_retention, summary.token_metrics.score_delta),
        reverse=True
    )

def render_leaderboard(evaluation_summaries: List[ModelEvaluationResult]) -> List[str]:
    lines = [
        "## Global Leaderboard",
        "| Model | Judge | CR (%) | PR (%) | Score Δ |",
        "| :--- | :--- | :---: | :---: | :---: |"
    ]
    
    sorted_summaries = sort_summaries_for_leaderboard(evaluation_summaries)
    
    for summary in sorted_summaries:
        compression_ratio = summary.token_metrics.compression_ratio
        performance_retention = summary.token_metrics.performance_retention
        score_delta = summary.token_metrics.score_delta
        lines.append(f"| `{summary.candidate_id}` | `{summary.judge_id}` | {compression_ratio:.1f} | {performance_retention:.1f} | {score_delta:+.2f} |")
        
    lines.append("\n---\n")
    return lines

def render_model_card(result: ModelEvaluationResult) -> List[str]:
    compression_ratio = result.token_metrics.compression_ratio
    performance_retention = result.token_metrics.performance_retention
    score_delta = result.token_metrics.score_delta
    average_source_tokens = result.token_metrics.average_source_tokens
    average_ers_tokens = result.token_metrics.average_ers_tokens
    sample_count = result.token_metrics.sample_count
    
    ers_percentage = PERCENTAGE_MULTIPLIER - compression_ratio
    
    card_lines = [
        f"### Candidate: `{result.candidate_id}`",
        f"**Judge:** `{result.judge_id}` | **Samples Evaluated:** {sample_count}\n",
        "#### System Metrics",
        "| Metric | Value |",
        "| :--- | :--- |",
        f"| **Compression Ratio (CR)** | {compression_ratio:.1f}% |",
        f"| **Performance Retention (PR)** | {performance_retention:.1f}% |",
        f"| **Score Δ** | {score_delta:+.2f} |",
        f"| **Avg Context Size** | {average_source_tokens:.0f} → {average_ers_tokens:.0f} tokens ({ers_percentage:.1f}% of original) |",
        "\n#### Answer Correctness",
        "| Dimension / Slice | Source Score | ERS Score | Δ |",
        "| :--- | :---: | :---: | :---: |"
    ]
    
    for row in result.score_breakdown:
        card_lines.append(f"| {row.label} | {row.source_score:.2f} | {row.ers_score:.2f} | {row.delta:+.2f} |")
        
    card_lines.append("\n---\n")
    return card_lines

def render_detailed_analysis(evaluation_summaries: List[ModelEvaluationResult]) -> List[str]:
    lines = ["## Detailed Analysis"]
    for summary in evaluation_summaries:
        lines.extend(render_model_card(summary))
    return lines

def render_full_report(evaluation_summaries: List[ModelEvaluationResult]) -> str:
    markdown_lines = []
    markdown_lines.extend(render_report_header())
    
    if evaluation_summaries:
        markdown_lines.extend(render_leaderboard(evaluation_summaries))
        markdown_lines.extend(render_detailed_analysis(evaluation_summaries))
    else:
        markdown_lines.append("\n> No evaluation data found to generate detailed analysis.")

    return "\n".join(markdown_lines)

def persist_report(content: str) -> None:
    PATHS["RESULTS_DIR"].mkdir(parents=True, exist_ok=True)
    report_path = PATHS["RESULTS_DIR"] / "report.md"
    with open(report_path, "w", encoding="utf-8") as report_file:
        report_file.write(content)

def build_reports(records: List[QuestionRecord], benchmark_results: Dict[str, Dict[str, List]]) -> None:
    evaluation_summaries = collect_evaluation_summaries(records, benchmark_results)
    report_content = render_full_report(evaluation_summaries)
    persist_report(report_content)
