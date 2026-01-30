-- SCT-6789
-- Description: Create product_reviews table
-- Author: Sushant
-- Date: 2026-01-30

BEGIN;

CREATE TABLE IF NOT EXISTS product_reviews (
    review_id BIGSERIAL PRIMARY KEY,
    product_id BIGINT NOT NULL,
    user_id BIGINT NOT NULL,
    review_text TEXT,
    rating INT CHECK (rating >= 1 AND rating <= 5),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

COMMIT;
