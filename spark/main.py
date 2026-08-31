from spark.reader import read_uber_data
from spark.reports import (
    revenue_analysis,
    busiest_pickup_hours
)

df = read_uber_data()
spark = df.sparkSession

print("=" * 60)
print("UBER SPARK ANALYTICS")
print("=" * 60)

revenue_analysis(df)

busiest_pickup_hours(df)

spark.stop()