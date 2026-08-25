KPI_QUERY = """
SELECT
    COUNT(*) AS total_trips,
    ROUND(CAST(SUM(total_amount) AS NUMERIC), 2) AS total_revenue,
    ROUND(CAST(AVG(fare_amount) AS NUMERIC), 2) AS average_fare,
    ROUND(CAST(AVG(trip_distance) AS NUMERIC), 2) AS average_distance,
    ROUND(CAST(AVG(passenger_count) AS NUMERIC), 2) AS average_passengers
FROM warehouse.fact_trips;
"""


PAYMENT_QUERY = """
SELECT
    CASE
        WHEN payment_type = 1 THEN 'Credit Card'
        WHEN payment_type = 2 THEN 'Cash'
        WHEN payment_type = 3 THEN 'No Charge'
        WHEN payment_type = 4 THEN 'Dispute'
        ELSE 'Unknown'
    END AS payment_method,
    COUNT(*) AS trips,
    ROUND(CAST(SUM(total_amount) AS NUMERIC), 2) AS revenue,
    ROUND(CAST(AVG(fare_amount) AS NUMERIC), 2) AS average_fare
FROM warehouse.fact_trips
GROUP BY payment_type
ORDER BY revenue DESC;
"""


VENDOR_QUERY = """
SELECT
    vendor_id,
    COUNT(*) AS trips,
    ROUND(CAST(SUM(total_amount) AS NUMERIC), 2) AS revenue,
    ROUND(CAST(AVG(fare_amount) AS NUMERIC), 2) AS average_fare,
    ROUND(CAST(AVG(trip_distance) AS NUMERIC), 2) AS average_distance
FROM warehouse.fact_trips
GROUP BY vendor_id
ORDER BY revenue DESC;
"""


TOP_PICKUP_QUERY = """
SELECT
    pickup_location,
    COUNT(*) AS trips
FROM warehouse.fact_trips
GROUP BY pickup_location
ORDER BY trips DESC
LIMIT 10;
"""


TOP_ROUTES_QUERY = """
SELECT
    CONCAT(
        pickup_location,
        ' → ',
        dropoff_location
    ) AS route,
    COUNT(*) AS trips,
    ROUND(
        CAST(AVG(total_amount) AS NUMERIC),
        2
    ) AS average_fare
FROM warehouse.fact_trips
GROUP BY pickup_location, dropoff_location
ORDER BY trips DESC
LIMIT 10;
"""


DISTANCE_QUERY = """
SELECT
    trip_distance
FROM warehouse.fact_trips
WHERE trip_distance > 0
  AND trip_distance <= 50;
"""


FARE_QUERY = """
SELECT
    fare_amount
FROM warehouse.fact_trips
WHERE fare_amount > 0
  AND fare_amount <= 200;
"""


DISTANCE_FARE_QUERY = """
SELECT
    trip_distance,
    total_amount,
    passenger_count
FROM warehouse.fact_trips
WHERE trip_distance > 0
  AND trip_distance <= 50
  AND total_amount > 0
  AND total_amount <= 300;
"""


VENDOR_LIST_QUERY = """
SELECT DISTINCT vendor_id
FROM warehouse.fact_trips
WHERE vendor_id IS NOT NULL
ORDER BY vendor_id;
"""


PAYMENT_LIST_QUERY = """
SELECT DISTINCT payment_type
FROM warehouse.fact_trips
WHERE payment_type IS NOT NULL
ORDER BY payment_type;
"""