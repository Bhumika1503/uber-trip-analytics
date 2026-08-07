CREATE TABLE IF NOT EXISTS warehouse.dim_vendor (
    vendor_key SERIAL PRIMARY KEY,
    vendor_id INT UNIQUE,
    vendor_name VARCHAR(100)
);

INSERT INTO warehouse.dim_vendor (
    vendor_id,
    vendor_name
)
SELECT DISTINCT
    "VendorID",
    CASE
        WHEN "VendorID" = 1 THEN 'Creative Mobile Technologies'
        WHEN "VendorID" = 2 THEN 'VeriFone'
        ELSE 'Unknown'
    END
FROM public.stg_yellow_tripdata
ON CONFLICT (vendor_id) DO NOTHING;