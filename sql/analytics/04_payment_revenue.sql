SELECT

p.payment_description,

ROUND(SUM(f.total_amount)::numeric,2) AS revenue

FROM warehouse.fact_trips f

JOIN warehouse.dim_payment p

ON f.payment_type = p.payment_type_id

GROUP BY p.payment_description

ORDER BY revenue DESC;