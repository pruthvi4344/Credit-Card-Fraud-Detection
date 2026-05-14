import pandas as pd
import numpy as np
from pathlib import Path

def generate_dataset(n=5000, fraud_rate=0.02, seed=42):
    np.random.seed(seed)
    amounts = np.random.exponential(scale=100, size=n)
    hours = np.random.randint(0, 24, size=n)
    countries = np.random.choice([0, 1], size=n, p=[0.9, 0.1])  # 1 = foreign
    y = (np.random.rand(n) < fraud_rate).astype(int)

    # Inject suspicious patterns
    amounts[y == 1] *= 8
    countries[y == 1] = 1
    hours[y == 1] = np.random.choice([0, 1, 2, 3, 4], size=(y == 1).sum())

    return pd.DataFrame({
        "amount": amounts,
        "hour": hours,
        "is_foreign": countries,
        "is_fraud": y
    })

if __name__ == "__main__":
    out = Path("data/raw/transactions.csv")
    out.parent.mkdir(parents=True, exist_ok=True)
    generate_dataset().to_csv(out, index=False)
    print(f"Saved dataset to {out}")