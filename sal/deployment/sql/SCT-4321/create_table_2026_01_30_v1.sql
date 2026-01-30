-- SCT-4321
-- Description: Create customer_feedback table
-- Author: Sushant
-- Date: 2026-01-30

BEGIN;

CREATE TABLE IF NOT EXISTS customer_feedback (
    feedback_id BIGSERIAL PRIMARY KEY,
    customer_id BIGINT NOT NULL,
    feedback_text TEXT,
    rating INT CHECK (rating >= 1 AND rating <= 5),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

COMMIT;
