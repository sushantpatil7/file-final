-- SCT-9067
-- Description: Create products table with sample data
-- Author: Sushant
-- Date: 2026-01-30

BEGIN;

CREATE TABLE IF NOT EXISTS products (
    product_id BIGSERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price NUMERIC(10,2) NOT NULL CHECK (price >= 0),
    stock INT DEFAULT 0
);

-- Insert sample data
INSERT INTO products (name, category, price, stock) VALUES
('Laptop', 'Electronics', 750.00, 10),
('Smartphone', 'Electronics', 500.00, 25),
('T-shirt', 'Fashion', 20.00, 100),
('Coffee Mug', 'Home & Kitchen', 12.50, 50);

COMMIT;
