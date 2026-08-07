CREATE SCHEMA IF NOT EXISTS warehouse;

CREATE TABLE IF NOT EXISTS warehouse.dim_payment (
    payment_key SERIAL PRIMARY KEY,
    payment_type_id INT UNIQUE,
    payment_description VARCHAR(50)
);

INSERT INTO warehouse.dim_payment (
    payment_type_id,
    payment_description
)
SELECT DISTINCT
    payment_type,
    CASE payment_type
        WHEN 1 THEN 'Credit Card'
        WHEN 2 THEN 'Cash'
        WHEN 3 THEN 'No Charge'
        WHEN 4 THEN 'Dispute'
        WHEN 5 THEN 'Unknown'
        WHEN 6 THEN 'Voided Trip'
        ELSE 'Other'
    END
FROM public.stg_yellow_tripdata
ON CONFLICT (payment_type_id) DO NOTHING;