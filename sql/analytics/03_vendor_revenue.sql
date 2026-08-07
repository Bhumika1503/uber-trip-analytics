SELECT

v.vendor_name,

ROUND(SUM(f.total_amount)::numeric,2) AS revenue

FROM warehouse.fact_trips f

JOIN warehouse.dim_vendor v

ON f.vendor_id = v.vendor_id

GROUP BY v.vendor_name

ORDER BY revenue DESC;