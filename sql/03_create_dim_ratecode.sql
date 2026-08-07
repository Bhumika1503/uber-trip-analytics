CREATE TABLE IF NOT EXISTS warehouse.dim_ratecode (
    ratecode_key SERIAL PRIMARY KEY,
    ratecode_id INT UNIQUE,
    rate_description VARCHAR(100)
);

INSERT INTO warehouse.dim_ratecode (
    ratecode_id,
    rate_description
)
SELECT DISTINCT
    "RatecodeID",
    CASE
        WHEN "RatecodeID" = 1 THEN 'Standard Rate'
        WHEN "RatecodeID" = 2 THEN 'JFK'
        WHEN "RatecodeID" = 3 THEN 'Newark'
        WHEN "RatecodeID" = 4 THEN 'Nassau/Westchester'
        WHEN "RatecodeID" = 5 THEN 'Negotiated Fare'
        WHEN "RatecodeID" = 6 THEN 'Group Ride'
        ELSE 'Unknown'
    END
FROM public.stg_yellow_tripdata
ON CONFLICT (ratecode_id) DO NOTHING;