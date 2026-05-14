from pathlib import Path
BASE_DIR = Path(__file__).resolve().parents[2]
RAW_DATA = BASE_DIR / "data/raw/transactions.csv"
PROCESSED_DATA = BASE_DIR / "data/processed/scored_transactions.csv"
MODEL_PATH = BASE_DIR / "models/fraud_model.joblib"
METRICS_PATH = BASE_DIR / "reports/model_metrics.json"