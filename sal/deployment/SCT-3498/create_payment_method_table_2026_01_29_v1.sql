CREATE TABLE payment_method_master (
    payment_method_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    method_code VARCHAR(30) NOT NULL UNIQUE,
    method_name VARCHAR(100) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
