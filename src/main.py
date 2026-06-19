import pandas as pd
from datetime import datetime

from src.config.settings import (
    RAW_DATA,
    PROCESSED_DATA,
    MODEL_PATH,
    METRICS_PATH
)

from src.data.generate_data import generate_dataset

from src.features.build_features import build_features

from src.models.train import train_model

from src.models.predict import score_transactions

# display the summary
def display_summary(scored_df):

    total = len(scored_df)

    fraud_count = len(
        scored_df[scored_df["risk_level"] == "High"]
    )

    normal_count = total - fraud_count

    print("\n========== SUMMARY ==========")

    print(f"Total Transactions : {total}")

    print(f"Fraud Transactions : {fraud_count}")

    print(f"Normal Transactions: {normal_count}")

    if total > 0:

        percentage = (fraud_count / total) * 100

        print(f"Fraud Percentage   : {percentage:.2f}%")

    print("=============================\n")


def save_report(scored_df):

    report_path = "reports/fraud_report.csv"

    scored_df.to_csv(
        report_path,
        index=False
    )

    print(f"Report saved: {report_path}")


def main():

    print("\nStarting pipeline...")

    start_time = datetime.now()

    RAW_DATA.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    if not RAW_DATA.exists():

        print("Dataset not found.")

        print("Generating dataset...")

        generate_dataset().to_csv(
            RAW_DATA,
            index=False
        )

        print("Dataset generated.")

    print("Loading dataset...")

    df = pd.read_csv(RAW_DATA)

    print(f"Rows loaded: {len(df)}")

    print("Training model...")

    model, report = train_model(
        df,
        MODEL_PATH,
        METRICS_PATH
    )

    print("Building features...")

    X, _ = build_features(df)

    print("Scoring transactions...")

    scored = score_transactions(
        model,
        X
    )

    PROCESSED_DATA.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    scored.to_csv(
        PROCESSED_DATA,
        index=False
    )

    display_summary(scored)

    save_report(scored)

    end_time = datetime.now()

    duration = end_time - start_time

    print("\nPipeline completed successfully.")

    print(f"Processed data : {PROCESSED_DATA}")

    print(f"Metrics file   : {METRICS_PATH}")

    print(f"Execution time : {duration}")


if __name__ == "__main__":

    try:

        main()

    except Exception as error:

        print("\nError occurred:")

        print(error)
