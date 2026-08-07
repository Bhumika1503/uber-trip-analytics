from pyspark.sql.functions import (
    col,
    sum,
    round,
    hour,
    count
)

def revenue_by_payment(df):

    print("\nRevenue By Payment Type")

    (
        df.groupBy("payment_type")
        .agg(
            round(
                sum("total_amount"),
                2
            ).alias("Revenue")
        )
        .orderBy(col("Revenue").desc())
        .show()
    )


def busiest_pickup_hours(df):

    print("\nBusiest Pickup Hours")

    (
        df.withColumn(
            "pickup_hour",
            hour("tpep_pickup_datetime")
        )
        .groupBy("pickup_hour")
        .agg(
            count("*").alias("Trips")
        )
        .orderBy(col("Trips").desc())
        .show()
    )