CREATE TABLE IF NOT EXISTS warehouse.fact_trips (

    trip_id BIGSERIAL PRIMARY KEY,

    hvfhs_license_num VARCHAR(20) NOT NULL,

    dispatching_base_num VARCHAR(20),
    originating_base_num VARCHAR(20),

    request_datetime TIMESTAMP,
    on_scene_datetime TIMESTAMP,

    pickup_datetime TIMESTAMP NOT NULL,
    dropoff_datetime TIMESTAMP NOT NULL,

    pickup_date DATE,
    dropoff_date DATE,

    pickup_hour INTEGER,
    pickup_day VARCHAR(20),

    pickup_location INTEGER,
    dropoff_location INTEGER,

    trip_miles DOUBLE PRECISION,
    trip_time BIGINT,
    trip_duration_minutes DOUBLE PRECISION,

    base_passenger_fare DOUBLE PRECISION,
    tolls DOUBLE PRECISION,
    bcf DOUBLE PRECISION,
    sales_tax DOUBLE PRECISION,
    congestion_surcharge DOUBLE PRECISION,
    airport_fee DOUBLE PRECISION,
    tips DOUBLE PRECISION,
    driver_pay DOUBLE PRECISION,

    total_revenue DOUBLE PRECISION,

    shared_request_flag VARCHAR(5),
    shared_match_flag VARCHAR(5),

    wav_request_flag VARCHAR(5),
    wav_match_flag VARCHAR(5),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);