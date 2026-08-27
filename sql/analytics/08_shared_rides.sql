SELECT
    shared_request_flag,
    shared_match_flag,
    COUNT(*) AS trip_count
FROM warehouse.fact_trips
GROUP BY
    shared_request_flag,
    shared_match_flag
ORDER BY trip_count DESC;