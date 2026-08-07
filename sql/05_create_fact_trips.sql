TRUNCATE TABLE warehouse.fact_trips RESTART IDENTITY;

INSERT INTO warehouse.fact_trips (
    pickup_date,
    dropoff_date,
    vendor_id,
    payment_type,
    ratecode_id,
    pickup_location,
    dropoff_location,
    passenger_count,
    trip_distance,
    fare_amount,
    tip_amount,
    total_amount
)
SELECT
    DATE("tpep_pickup_datetime"),
    DATE("tpep_dropoff_datetime"),
    "VendorID",
    payment_type,
    "RatecodeID",
    "PULocationID",
    "DOLocationID",
    passenger_count,
    trip_distance,
    fare_amount,
    tip_amount,
    total_amount
FROM public.stg_yellow_tripdata;