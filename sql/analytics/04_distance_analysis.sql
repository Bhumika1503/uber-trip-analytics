SELECT
    ROUND(AVG(trip_miles)::numeric, 2) AS average_trip_miles,
    ROUND(MAX(trip_miles)::numeric, 2) AS maximum_trip_miles,

    ROUND(
        AVG(
            CASE
                WHEN trip_miles > 0
                THEN base_passenger_fare / trip_miles
            END
        )::numeric,
        2
    ) AS average_fare_per_mile

FROM warehouse.fact_trips
WHERE trip_miles >= 0;