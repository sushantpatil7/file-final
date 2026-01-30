-- SCT-5654
-- Description: Create order_audit table
-- Author: Sushant
-- Date: 2026-01-30

BEGIN;

CREATE TABLE IF NOT EXISTS order_audit (
    audit_id     BIGSERIAL PRIMARY KEY,
    order_id     BIGINT NOT NULL,
    status       VARCHAR(50) NOT NULL,
    updated_at   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by   VARCHAR(100)
);

COMMIT;
