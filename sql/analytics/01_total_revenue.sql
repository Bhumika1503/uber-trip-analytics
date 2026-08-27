SELECT
    COUNT(*) AS total_trips,
    ROUND(SUM(total_revenue)::numeric, 2) AS total_revenue,
    ROUND(AVG(total_revenue)::numeric, 2) AS average_trip_value
FROM warehouse.fact_trips;