SELECT
    ROUND(AVG(trip_duration_minutes)::numeric, 2)
        AS average_trip_duration_minutes,

    ROUND(
        PERCENTILE_CONT(0.5)
        WITHIN GROUP (ORDER BY trip_duration_minutes)::numeric,
        2
    ) AS median_trip_duration_minutes,

    ROUND(MAX(trip_duration_minutes)::numeric, 2)
        AS maximum_trip_duration_minutes

FROM warehouse.fact_trips
WHERE trip_duration_minutes >= 0;