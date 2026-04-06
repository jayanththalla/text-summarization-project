from pathlib import Path

# Get project root (2 levels up from this file: src/textsummarizer/constants)
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent

CONFIG_FILE_PATH = PROJECT_ROOT / "config" / "config.yaml"
PARAMS_FILE_PATH = PROJECT_ROOT / "params.yaml"
