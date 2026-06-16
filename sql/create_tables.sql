-- fraud detection table 
CREATE TABLE fraud_predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    amount REAL,
    fraud_probability REAL,
    risk_level TEXT
);

-- transaction table created
CREATE TABLE transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,

    card_number TEXT,
    customer_id INTEGER,

    amount REAL NOT NULL,

    merchant_name TEXT,

    transaction_time DATETIME,

    location TEXT,

    transaction_type TEXT,

    status TEXT
);

-- customer detials table
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,

    full_name TEXT,

    email TEXT UNIQUE,

    phone TEXT,

    city TEXT,

    country TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

--Stores ML model information.
CREATE TABLE models (
    model_id INTEGER PRIMARY KEY AUTOINCREMENT,

    model_name TEXT,

    version TEXT,

    accuracy REAL,

    precision_score REAL,

    recall_score REAL,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- user login
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT UNIQUE,

    password_hash TEXT,

    role TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- prediction history table (Keeps history of every prediction)
CREATE TABLE prediction_history (
    history_id INTEGER PRIMARY KEY AUTOINCREMENT,

    transaction_id INTEGER,

    fraud_probability REAL,

    risk_level TEXT,

    predicted_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (transaction_id)
    REFERENCES transactions(transaction_id)
);
