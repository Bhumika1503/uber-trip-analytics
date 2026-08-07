-- 1. Total Trips
SELECT COUNT(*) AS total_trips
FROM warehouse.fact_trips;

-- 2. Negative Trip Distance
SELECT COUNT(*) AS negative_distance
FROM warehouse.fact_trips
WHERE trip_distance < 0;

-- 3. Negative Fare
SELECT COUNT(*) AS negative_fare
FROM warehouse.fact_trips
WHERE fare_amount < 0;

-- 4. Missing Passenger Count
SELECT COUNT(*) AS missing_passengers
FROM warehouse.fact_trips
WHERE passenger_count IS NULL;

-- 5. Missing Payment Type
SELECT COUNT(*) AS missing_payment
FROM warehouse.fact_trips
WHERE payment_type IS NULL;

-- 6. Trips with Zero Distance
SELECT COUNT(*) AS zero_distance
FROM warehouse.fact_trips
WHERE trip_distance = 0;