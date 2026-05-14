# ERS_POC

## ARCHITECTURE
* logic_topology: `cli.py` -> `engine.py` -> {`metrics.py`, `report.py`}
* data_flow: HF_HUB -> records -> candidates -> evaluations -> markdown_reports
* identity_contract: task == {domain, sample_id, question_id} [composite_key]

## MODULES

### `cli.py`
* role: command_interface
* logic: `argparse` -> {`generate`, `evaluate`, `report`, `run-all`}
* mapping: user_input -> `run_x()` -> {`execute_x()` | `build_reports()`}
* feature: {concise_help, multi_model_support, autodetection: `discover_models_from_artifacts()`}
* invariant: `load_dotenv()` @ `main()`

### `engine.py`
* role: execution_orchestrator
* logic: `incremental_loop` + `atomic_persistence`
* flow:
    * `execute_generation()`: `filter_pending_generation_tasks()` -> `request_llm_completion()` -> `candidates/`
    * `execute_evaluation()`: `filter_pending_evaluation_tasks()` -> `evaluate_single_answer()` -> `evaluations/`
* mechanisms:
    * `request_llm_completion()`: `litellm` + tags: {`<START_CONTEXT>`, `<START_QUESTION>`} + retry: `tenacity`
    * `build_evaluation_metric()`: `GEval` + params: {INPUT, ACTUAL, EXPECTED}
    * `fetch_dataset()`: HF_HUB -> local_cache: `dataset.json`
    * `persist_x()`: {`json.dump()` -> tmp_file -> `replace()`} => data_integrity

### `report.py`
* role: metrics_engine + artifact_generator
* logic: `collect_evaluation_summaries()` -> `render_full_report()` -> `report.md`
* metrics:
    * **CR** [compression_ratio]: `(1.0 - (ers_tokens / src_tokens)) * 100`
    * **PR** [performance_retention]: `(ers_score / src_score) * 100`
    * **Delta** [score_delta]: `ers_score - src_score`
* structures:
    * `TokenMetrics`: {sample_count, compression_ratio, performance_retention, score_delta, avg_tokens}
    * `ModelEvaluationResult`: {candidate_id, judge_id, token_metrics, score_breakdown}
* mechanisms:
    * `BenchmarkDataIndex`: identity_tuple -> {record, generation}
    * `calculate_token_metrics()`: `tiktoken` -> {token_counts, score_averages}
    * `aggregate_domain_scores()`: group_by[{domain, question_type, context_type}]
    * `render_x()`: markdown_template_composition

### `models.py`
* role: domain_schema
* contract: identity_tuple == `(domain, sample_id, question_id)` -> composite_key
* entities:
    * `QuestionRecord`: {source, ers_artifact, question_type, question, answer}
    * `GenerationItem`: {context_type, actual_output, finish_reason, latency_ms, tokens, cost, model_id}
    * `EvaluationItem`: {context_type, score, reason, candidate_id, judge_id}

### `config.py`
* role: environment_registry
* constants: {HF_DATASET_PATH, LOCAL_DATASET_PATH, PATHS, TIKTOKEN_ENCODING}

### `prompts.py`
* role: semantic_instruction_layer
* constants:
    * CANDIDATE_SYSTEM_PROMPT: reasoning_extraction_logic
    * JUDGE_CRITERIA: {logical_alignment, logical_coverage, style_insensitivity}
