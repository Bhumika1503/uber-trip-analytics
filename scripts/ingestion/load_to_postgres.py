import traceback
import pandas as pd
from sqlalchemy import text
from config.database import engine

try:
    print("Reading Parquet file...")
    df = pd.read_parquet("data/raw/yellow_tripdata_2023-01.parquet")

    print(f"Rows Loaded: {len(df)}")

    # Only load a small sample first
    df = df.head(1000)

    print("Uploading sample to PostgreSQL...")

    df.to_sql(
        name="stg_yellow_tripdata",
        con=engine,
        if_exists="replace",
        index=False
    )

    print("✅ Upload Successful!")

except Exception:
    print("\n❌ ERROR OCCURRED:\n")
    traceback.print_exc()