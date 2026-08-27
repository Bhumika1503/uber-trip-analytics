from pyspark.sql import functions as F

from spark.reader import read_uber_data


def hourly_demand(df):
    """
    Number of trips by pickup hour.
    """

    return (
        df.groupBy("pickup_hour")
        .agg(
            F.count("*").alias("total_trips")
        )
        .orderBy("pickup_hour")
    )


def daily_demand(df):
    """
    Number of trips by day of week.
    """

    return (
        df.groupBy("pickup_day")
        .agg(
            F.count("*").alias("total_trips")
        )
        .orderBy(F.col("total_trips").desc())
    )


def revenue_analysis(df):
    """
    Revenue and driver-pay analysis.
    """

    return (
        df.agg(
            F.count("*").alias("total_trips"),
            F.round(
                F.sum("total_revenue"), 2
            ).alias("total_revenue"),
            F.round(
                F.avg("total_revenue"), 2
            ).alias("average_trip_value"),
            F.round(
                F.sum("tips"), 2
            ).alias("total_tips"),
            F.round(
                F.sum("driver_pay"), 2
            ).alias("total_driver_pay"),
            F.round(
                F.avg("base_passenger_fare"), 2
            ).alias("average_base_fare")
        )
    )


def trip_analysis(df):
    """
    Distance and duration analysis.
    """

    return (
        df.agg(
            F.round(
                F.avg(F.col("trip_miles")),
                2
            ).alias("average_distance"),

            F.round(
                F.max(F.col("trip_miles")),
                2
            ).alias("max_distance"),

            F.round(
                F.avg(F.col("trip_duration_minutes")),
                2
            ).alias("average_duration"),

            F.round(
                F.max(F.col("trip_duration_minutes")),
                2
            ).alias("max_duration"),

            F.round(
                F.avg(
                    F.when(
                        F.col("trip_duration_minutes") > 0,
                        F.col("trip_miles") /
                        F.col("trip_duration_minutes")
                    )
                ),
                2
            ).alias("average_miles_per_minute")
        )
    )


def top_pickup_locations(df, limit=10):
    """
    Top pickup locations by trip count.
    """

    return (
        df.groupBy("pickup_location")
        .agg(
            F.count("*").alias("total_trips")
        )
        .orderBy(
            F.col("total_trips").desc()
        )
        .limit(limit)
    )


def top_dropoff_locations(df, limit=10):
    """
    Top drop-off locations by trip count.
    """

    return (
        df.groupBy("dropoff_location")
        .agg(
            F.count("*").alias("total_trips")
        )
        .orderBy(
            F.col("total_trips").desc()
        )
        .limit(limit)
    )


def shared_ride_analysis(df):
    """
    Shared ride request and match analysis.
    """

    return (
        df.agg(
            F.sum(
                F.when(
                    F.col("shared_request_flag") == "Y",
                    1
                ).otherwise(0)
            ).alias("shared_requests"),

            F.sum(
                F.when(
                    F.col("shared_match_flag") == "Y",
                    1
                ).otherwise(0)
            ).alias("shared_matches"),

            F.sum(
                F.when(
                    F.col("wav_request_flag") == "Y",
                    1
                ).otherwise(0)
            ).alias("wav_requests"),

            F.sum(
                F.when(
                    F.col("wav_match_flag") == "Y",
                    1
                ).otherwise(0)
            ).alias("wav_matches")
        )
    )


if __name__ == "__main__":

    print("=" * 60)
    print("UBER SPARK ANALYTICS")
    print("=" * 60)

    df = read_uber_data()

    print(f"\nTotal Records: {df.count()}")

    print("\n--- HOURLY DEMAND ---")
    hourly_demand(df).show()

    print("\n--- DAILY DEMAND ---")
    daily_demand(df).show()

    print("\n--- REVENUE ANALYSIS ---")
    revenue_analysis(df).show()

    print("\n--- TRIP ANALYSIS ---")
    trip_analysis(df).show()

    print("\n--- TOP PICKUP LOCATIONS ---")
    top_pickup_locations(df).show()

    print("\n--- TOP DROP-OFF LOCATIONS ---")
    top_dropoff_locations(df).show()

    print("\n--- SHARED RIDE ANALYSIS ---")
    shared_ride_analysis(df).show()

    df.sparkSession.stop()