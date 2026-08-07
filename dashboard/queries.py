

KPI_QUERY = """
SELECT
    COUNT(*) AS total_trips,
    ROUND(CAST(SUM(total_amount) AS NUMERIC),2) AS total_revenue,
    ROUND(CAST(AVG(fare_amount) AS NUMERIC),2) AS average_fare,
    ROUND(CAST(AVG(trip_distance) AS NUMERIC),2) AS average_distance
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

ROUND(CAST(SUM(total_amount) AS NUMERIC),2) AS revenue

FROM warehouse.fact_trips

GROUP BY payment_method

ORDER BY revenue DESC;
"""


VENDOR_QUERY = """
SELECT
vendor_id,
COUNT(*) AS trips
FROM warehouse.fact_trips
GROUP BY vendor_id
ORDER BY trips DESC;
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



DISTANCE_QUERY = """
SELECT
vendor_id,
ROUND(CAST(AVG(trip_distance) AS NUMERIC),2) AS avg_distance
FROM warehouse.fact_trips
GROUP BY vendor_id
ORDER BY avg_distance DESC;
"""