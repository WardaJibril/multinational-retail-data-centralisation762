BEGIN;

ALTER TABLE dim_products
ALTER COLUMN product_price TYPE TEXT;
UPDATE dim_products
	
SET product_price = REPLACE(product_price, '£', '')
WHERE product_price LIKE '£%';


ALTER TABLE dim_products
ALTER COLUMN product_price TYPE NUMERIC USING product_price::NUMERIC;


ALTER TABLE dim_products
ADD COLUMN weight_class VARCHAR(20);


UPDATE dim_products
SET weight_class = CASE
    WHEN weight < 2 THEN 'Light'
    WHEN weight >= 2 AND weight < 40 THEN 'Mid_Sized'
    WHEN weight >= 40 AND weight < 140 THEN 'Heavy'
    WHEN weight >= 140 THEN 'Truck_Required'
    ELSE 'Unknown'
END;

COMMIT;

