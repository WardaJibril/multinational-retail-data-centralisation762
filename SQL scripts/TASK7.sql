
SELECT MAX(LENGTH(card_number:: TEXT)) FROM dim_card_details;

SELECT MAX(LENGTH(expiry_date:: TEXT)) FROM dim_card_details;

-- run each code black separately, with BEGIN and COMMIT clauses to commit the changes

UPDATE dim_card_details
SET date_payment_confirmed = NULL
WHERE date_payment_confirmed::TEXT = '';



ALTER TABLE dim_card_details
    ALTER COLUMN card_number TYPE VARCHAR(22);

ALTER TABLE dim_card_details
    ALTER COLUMN expiry_date TYPE VARCHAR(10);

ALTER TABLE dim_card_details
    ALTER COLUMN date_payment_confirmed TYPE DATE USING date_payment_confirmed::DATE;