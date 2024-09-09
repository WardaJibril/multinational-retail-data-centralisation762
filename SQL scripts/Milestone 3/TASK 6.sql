SELECT MAX(LENGTH(day:: TEXT)) FROM dim_date_times

SELECT MAX(LENGTH(month:: TEXT)) FROM dim_date_times

SELECT MAX(LENGTH(year:: TEXT)) FROM dim_date_times

SELECT MAX(LENGTH(time_period:: TEXT)) FROM dim_date_times

BEGIN;

ALTER TABLE dim_date_times
   ALTER COLUMN day  TYPE VARCHAR(2),
   ALTER COLUMN month TYPE VARCHAR(2),
   ALTER COLUMN year TYPE VARCHAR(4),
   ALTER COLUMN time_period TYPE VARCHAR(10),
   ALTER COLUMN date_uuid TYPE UUID USING date_uuid:: UUID;

COMMIT;