import pandas as pd

def build_features(df: pd.DataFrame):
    X = df[["amount", "hour", "is_foreign"]].copy()
    X["amount_log"] = X["amount"].apply(lambda x: 0 if x <= 0 else __import__("math").log1p(x))
    y = df["is_fraud"]
    return X, y