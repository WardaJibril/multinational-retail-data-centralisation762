--TASK1: Cast coloumns of orders_table to correct data types

--find max length
SELECT MAX(LENGTH(CAST(card_number AS TEXT))) FROM orders_table;
--19
SELECT MAX(LENGTH(CAST(store_code AS TEXT))) FROM orders_table;
--12
SELECT MAX(LENGTH(CAST(product_code AS TEXT))) FROM orders_table;
--11

-- change data types
BEGIN;

ALTER TABLE orders_table
ALTER COLUMN date_uuid TYPE UUID USING date_uuid::UUID,
ALTER COLUMN user_uuid TYPE UUID USING user_uuid::UUID,
ALTER COLUMN card_number TYPE VARCHAR(19),
ALTER COLUMN store_code TYPE VARCHAR(12),
ALTER COLUMN product_code TYPE VARCHAR(11),
ALTER COLUMN product_quantity TYPE SMALLINT;

COMMIT;

--confirm data types
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'orders_table';