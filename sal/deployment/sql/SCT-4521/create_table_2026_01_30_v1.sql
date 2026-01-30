-- SCT-4521
-- Description: Create example table
-- Author: Sushant
-- Date: 2026-01-30

BEGIN;

CREATE TABLE IF NOT EXISTS example_table (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

COMMIT;
