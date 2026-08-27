SELECT
    pickup_location,
    dropoff_location,
    COUNT(*) AS trip_count
FROM warehouse.fact_trips
GROUP BY
    pickup_location,
    dropoff_location
ORDER BY trip_count DESC
LIMIT 10;