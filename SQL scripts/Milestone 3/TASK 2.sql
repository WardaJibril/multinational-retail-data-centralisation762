SELECT MAX(LENGTH(CAST(country_code AS TEXT))) FROM dim_users;

BEGIN;

ALTER TABLE dim_users
ALTER COLUMN first_name TYPE VARCHAR(255),
ALTER COLUMN last_name TYPE VARCHAR(255),
ALTER COLUMN date_of_birth TYPE DATE,
ALTER COLUMN country_code TYPE VARCHAR(2),
ALTER COLUMN user_uuid TYPE UUID USING user_uuid::UUID,
ALTER COLUMN join_date TYPE DATE;

COMMIT;

SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'dim_users';