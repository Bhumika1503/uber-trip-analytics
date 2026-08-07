import pandas as pd

# Read the parquet file
df = pd.read_parquet("data/raw/yellow_tripdata_2023-01.parquet")

# Display first 5 rows
print("\n========== FIRST 5 ROWS ==========\n")
print(df.head())

# Shape
print("\n========== DATASET SHAPE ==========\n")
print(df.shape)

# Column Names
print("\n========== COLUMN NAMES ==========\n")
print(df.columns.tolist())

# Data Types
print("\n========== DATA TYPES ==========\n")
print(df.dtypes)