SELECT
    ROUND(SUM(total_amount)::numeric,2) AS total_revenue
FROM warehouse.fact_trips;