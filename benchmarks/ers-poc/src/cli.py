import argparse
from typing import List, Optional

from .config import PATHS
from .engine import (
    execute_evaluation,
    execute_generation,
    fetch_all_evaluations,
    fetch_dataset,
    fetch_generations,
)
from .report import build_reports


def build_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="ERS-POC: ERS Efficiency Benchmark",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  ./run.sh run-all --models gpt-4o gemma-2-9b --judge-model gpt-4o
  ./run.sh generate --models llama-3.1-8b --limit 5
  ./run.sh report"""
    )

    subparsers = parser.add_subparsers(dest="command", required=True, metavar="CMD")

    def add_common_arguments(subparser: argparse.ArgumentParser) -> None:
        subparser.add_argument("--models", nargs="+", required=True, metavar="ID", help="Model IDs")
        subparser.add_argument("--limit", type=int, metavar="N", help="Limit samples")

    generate_parser = subparsers.add_parser("generate", help="Fetch responses")
    add_common_arguments(generate_parser)

    evaluate_parser = subparsers.add_parser("evaluate", help="Score responses")
    add_common_arguments(evaluate_parser)
    evaluate_parser.add_argument("--judge-model", metavar="ID", help="Judge ID")

    report_parser = subparsers.add_parser("report", help="Build reports")
    report_parser.add_argument("--models", nargs="+", metavar="ID", help="Model IDs")
    report_parser.add_argument("--limit", type=int, metavar="N", help="Limit samples")

    run_all_parser = subparsers.add_parser("run-all", help="Full pipeline")
    add_common_arguments(run_all_parser)
    run_all_parser.add_argument("--judge-model", metavar="ID", help="Judge ID")

    return parser


def run_generation(models: List[str], limit: Optional[int] = None) -> None:
    for model in models:
        print(f"Generating for model: {model} (limit: {limit})")
        execute_generation(model, limit)


def run_evaluation(models: List[str], limit: Optional[int], judge_model: Optional[str]) -> None:
    for model in models:
        judge_id = judge_model if judge_model else "DeepEval default"
        print(f"Evaluating for model: {model} (limit: {limit}, judge: {judge_id})")
        execute_evaluation(model, limit, judge_model)


def run_reporting(models: Optional[List[str]] = None, limit: Optional[int] = None) -> None:
    target_models = models if models else discover_models_from_artifacts()

    if not target_models:
        print("No evaluation data found. Run 'generate' and 'evaluate' first.")
        return

    records = fetch_dataset(limit)
    benchmark_results = {}

    print(f"Aggregating data for models: {', '.join(target_models)}")
    for model in target_models:
        generations = fetch_generations(model)
        evaluations_dict = fetch_all_evaluations(model)
        
        if generations or evaluations_dict:
            benchmark_results[model] = {
                "generations": generations,
                "evaluations": evaluations_dict
            }

    if not benchmark_results:
        print("No valid data found for the specified/discovered models.")
        return

    print("Building reports...")
    build_reports(records, benchmark_results)
    print("Reports generated in results directory.")


def discover_models_from_artifacts() -> List[str]:
    discovered_models = set()

    if PATHS["CANDIDATES_DIR"].exists():
        for candidate_file in PATHS["CANDIDATES_DIR"].glob("*_candidate.json"):
            model_id = candidate_file.name.replace("_candidate.json", "")
            discovered_models.add(model_id)

    if PATHS["EVALS_DIR"].exists():
        for evaluation_file in PATHS["EVALS_DIR"].glob("*_evaluations.json"):
            filename_parts = evaluation_file.name.split("_")
            if len(filename_parts) >= 2:
                discovered_models.add(filename_parts[0])

    return sorted(list(discovered_models))


def main() -> None:
    from dotenv import load_dotenv
    load_dotenv()

    parser = build_argument_parser()
    args = parser.parse_args()

    if args.command == "generate":
        run_generation(args.models, args.limit)
    elif args.command == "evaluate":
        run_evaluation(args.models, args.limit, args.judge_model)
    elif args.command == "report":
        run_reporting(args.models, args.limit)
    elif args.command == "run-all":
        run_generation(args.models, args.limit)
        run_evaluation(args.models, args.limit, args.judge_model)
        run_reporting(args.models, args.limit)


if __name__ == "__main__":
    main()
