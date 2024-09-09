BEGIN;
UPDATE dim_store_details
SET latitude = lat  
WHERE latitude IS NULL;

ALTER TABLE dim_store_details
DROP COLUMN lat;



ALTER TABLE dim_store_details
    ALTER COLUMN longitude TYPE FLOAT USING longitude::FLOAT,
    ALTER COLUMN locality TYPE VARCHAR(255),
    ALTER COLUMN store_code TYPE VARCHAR(11),
    ALTER COLUMN staff_numbers TYPE SMALLINT,
    ALTER COLUMN opening_date TYPE DATE USING opening_date::DATE,
    ALTER COLUMN store_type TYPE VARCHAR(255),
    ALTER COLUMN latitude TYPE FLOAT USING latitude::FLOAT,
    ALTER COLUMN country_code TYPE VARCHAR(10), 
    ALTER COLUMN continent TYPE VARCHAR(255);


UPDATE dim_store_details
SET locality = NULL
WHERE locality = 'N/A';

COMMIT;

SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'dim_store_details'

