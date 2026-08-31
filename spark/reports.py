from pyspark.sql.functions import col, sum, round, count


def revenue_analysis(df):

    print("\nRevenue Analysis")

    (
        df.agg(
            round(
                sum("total_revenue"),
                2
            ).alias("Total Revenue")
        )
        .show()
    )


def busiest_pickup_hours(df):

    print("\nBusiest Pickup Hours")

    (
        df.groupBy("pickup_hour")
        .agg(
            count("*").alias("Trips")
        )
        .orderBy(col("Trips").desc())
        .show()
    )