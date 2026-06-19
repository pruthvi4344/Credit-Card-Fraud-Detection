import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from src.config.settings import MODEL_PATH
from src.models.predict import assign_risk

# implemented fastapi
app = FastAPI(title="Fraud Detection API")

# defining transaction class
class Transaction(BaseModel):
    amount: float
    hour: int
    is_foreign: int

@app.on_event("startup")
def load_model():
    global model
    model = joblib.load(MODEL_PATH)

# score function
@app.post("/score")
def score(tx: Transaction):
    df = pd.DataFrame([{
        "amount": tx.amount,
        "hour": tx.hour,
        "is_foreign": tx.is_foreign,
        "amount_log": __import__("math").log1p(max(tx.amount, 0))
    }])
    prob = float(model.predict_proba(df)[0, 1])
    return {
        "fraud_probability": prob,
        "risk_level": assign_risk(prob)
    }
