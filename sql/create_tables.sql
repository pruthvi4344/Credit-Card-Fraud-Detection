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
