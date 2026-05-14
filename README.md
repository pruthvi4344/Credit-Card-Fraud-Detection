# Credit Card Transaction Fraud Detection

## Project Overview
A production-style machine learning system for detecting fraudulent credit card transactions and assigning risk levels.

This project simulates how banks and fintech companies detect suspicious activity in real time. It covers data preprocessing, feature engineering, model training, evaluation, SQL storage, and an API for scoring new transactions.

## Business Problem
Financial institutions process millions of transactions daily. Fraud represents a tiny percentage of activity but causes significant losses. The goal is to identify high-risk transactions with high recall while minimizing false positives.

## Architecture
1. Raw transaction data ingestion
2. Data cleaning and validation
3. Feature engineering
4. Model training (Random Forest baseline)
5. Risk scoring
6. SQL persistence
7. FastAPI scoring endpoint
8. Dashboard/reporting

## Technology Stack
- Python
- Pandas, NumPy
- Scikit-learn
- FastAPI
- SQLite
- Docker
- Pytest

## Setup
```bash
git clone <repo-url>
cd credit-card-fraud-detection
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python src/main.py
```

## Run API
```bash
uvicorn src.api.app:app --reload
```

## Run Tests
```bash
pytest
```

## Sample Outputs
- `reports/model_metrics.json`
- `data/processed/scored_transactions.csv`

## Future Enhancements
- XGBoost and LightGBM
- Feature store
- Real-time Kafka ingestion
- Power BI dashboard
