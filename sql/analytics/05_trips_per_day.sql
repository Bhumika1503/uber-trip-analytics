SELECT

pickup_date,

COUNT(*) AS total_trips

FROM warehouse.fact_trips

GROUP BY pickup_date

ORDER BY pickup_date;