from pathlib import Path

HF_DATASET_PATH = "alxraun/ers-bench-nano"

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RESULTS_DIR = BASE_DIR / "results"
CANDIDATES_DIR = RESULTS_DIR / "candidates"
EVALS_DIR = RESULTS_DIR / "evaluations"

LOCAL_DATASET_PATH = DATA_DIR / "dataset.json"

PATHS = {
    "DATA_DIR": DATA_DIR,
    "RESULTS_DIR": RESULTS_DIR, 
    "CANDIDATES_DIR": CANDIDATES_DIR, 
    "EVALS_DIR": EVALS_DIR
}

TIKTOKEN_ENCODING = "o200k_base"
