from reader import read_data
from reports import (
    revenue_by_payment,
    busiest_pickup_hours
)

spark, df = read_data()

print("=" * 60)
print("UBER SPARK ANALYTICS")
print("=" * 60)

revenue_by_payment(df)

busiest_pickup_hours(df)

spark.stop()