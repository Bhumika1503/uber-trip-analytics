SELECT
    COUNT(*) AS total_trips
FROM warehouse.fact_trips;


SELECT
    hvfhs_license_num,
    COUNT(*) AS trip_count
FROM warehouse.fact_trips
GROUP BY hvfhs_license_num;


SELECT
    COUNT(*) AS missing_datetime_records
FROM warehouse.fact_trips
WHERE pickup_datetime IS NULL
   OR dropoff_datetime IS NULL;


SELECT
    COUNT(*) AS invalid_distance_records
FROM warehouse.fact_trips
WHERE trip_miles < 0;


SELECT
    COUNT(*) AS invalid_duration_records
FROM warehouse.fact_trips
WHERE trip_time < 0;