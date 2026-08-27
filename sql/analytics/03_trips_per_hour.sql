SELECT
    pickup_hour,
    COUNT(*) AS trip_count
FROM warehouse.fact_trips
GROUP BY pickup_hour
ORDER BY pickup_hour;