CREATE TABLE IF NOT EXISTS warehouse.dim_date (
    date_key DATE PRIMARY KEY,
    year INT,
    month INT,
    day INT,
    quarter INT,
    day_of_week INT
);

INSERT INTO warehouse.dim_date (
    date_key,
    year,
    month,
    day,
    quarter,
    day_of_week
)
SELECT DISTINCT
    DATE("tpep_pickup_datetime"),
    EXTRACT(YEAR FROM "tpep_pickup_datetime")::INT,
    EXTRACT(MONTH FROM "tpep_pickup_datetime")::INT,
    EXTRACT(DAY FROM "tpep_pickup_datetime")::INT,
    EXTRACT(QUARTER FROM "tpep_pickup_datetime")::INT,
    EXTRACT(DOW FROM "tpep_pickup_datetime")::INT
FROM public.stg_yellow_tripdata
ON CONFLICT (date_key) DO NOTHING;