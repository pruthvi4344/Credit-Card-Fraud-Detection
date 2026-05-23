-- fraud detection table created
CREATE TABLE fraud_predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL,
    fraud_probability REAL,
    risk_level TEXT
);
