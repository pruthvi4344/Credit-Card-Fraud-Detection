import pandas as pd
from src.config.settings import RAW_DATA, PROCESSED_DATA, MODEL_PATH, METRICS_PATH
from src.data.generate_data import generate_dataset
from src.features.build_features import build_features
from src.models.train import train_model
from src.models.predict import score_transactions

def main():
    RAW_DATA.parent.mkdir(parents=True, exist_ok=True)
    if not RAW_DATA.exists():
        generate_dataset().to_csv(RAW_DATA, index=False)

    df = pd.read_csv(RAW_DATA)
    model, report = train_model(df, MODEL_PATH, METRICS_PATH)

    X, _ = build_features(df)
    scored = score_transactions(model, X)
    PROCESSED_DATA.parent.mkdir(parents=True, exist_ok=True)
    scored.to_csv(PROCESSED_DATA, index=False)

    print("Pipeline completed successfully.")
    print(f"Scored data saved to {PROCESSED_DATA}")
    print(f"Metrics saved to {METRICS_PATH}")

if __name__ == "__main__":
    main()