SELECT
    ROUND(AVG(fare_amount)::numeric,2) AS average_fare
FROM warehouse.fact_trips;