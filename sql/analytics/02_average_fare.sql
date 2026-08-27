SELECT
    ROUND(AVG(base_passenger_fare)::numeric, 2) AS average_fare,
    ROUND(AVG(tips)::numeric, 2) AS average_tip,
    ROUND(AVG(driver_pay)::numeric, 2) AS average_driver_pay
FROM warehouse.fact_trips;