BEGIN;

ALTER TABLE dim_products
RENAME COLUMN removed TO still_available;

SELECT MAX(LENGTH("EAN")) FROM dim_products

SELECT MAX(LENGTH(product_code)) FROM dim_products

SELECT MAX(LENGTH(weight_class)) FROM dim_products

ALTER TABLE dim_products
    ALTER COLUMN weight TYPE FLOAT USING weight::FLOAT,
    ALTER COLUMN "EAN" TYPE VARCHAR(17),
    ALTER COLUMN product_code TYPE VARCHAR(11),
    ALTER COLUMN date_added TYPE DATE USING date_added::DATE,
    ALTER COLUMN uuid TYPE UUID USING uuid::UUID,
    ALTER COLUMN still_available TYPE BOOL USING (CASE WHEN still_available = 'true' THEN true ELSE false END),
    ALTER COLUMN weight_class TYPE VARCHAR(14);

COMMIT;