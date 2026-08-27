import pandas as pd

from config.logger import logger


def transform(df):

    logger.info("Transform Phase Started")

    print("Running Transformation...")

    df = df.copy()

    # ---------------------------------------------------------
    # Convert datetime columns
    # ---------------------------------------------------------

    datetime_columns = [
        "request_datetime",
        "on_scene_datetime",
        "pickup_datetime",
        "dropoff_datetime"
    ]

    for column in datetime_columns:

        df[column] = pd.to_datetime(
            df[column],
            errors="coerce"
        )

    # ---------------------------------------------------------
    # Convert numeric columns
    # ---------------------------------------------------------

    numeric_columns = [
        "pulocationid",
        "dolocationid",
        "trip_miles",
        "trip_time",
        "base_passenger_fare",
        "tolls",
        "bcf",
        "sales_tax",
        "congestion_surcharge",
        "airport_fee",
        "tips",
        "driver_pay"
    ]

    for column in numeric_columns:

        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

    # ---------------------------------------------------------
    # Create date and time analysis columns
    # ---------------------------------------------------------

    df["pickup_date"] = (
        df["pickup_datetime"].dt.date
    )

    df["dropoff_date"] = (
        df["dropoff_datetime"].dt.date
    )

    df["pickup_hour"] = (
        df["pickup_datetime"].dt.hour
    )

    df["pickup_day"] = (
        df["pickup_datetime"].dt.day_name()
    )

    # ---------------------------------------------------------
    # Trip duration in minutes
    # ---------------------------------------------------------

    df["trip_duration_minutes"] = (
        df["trip_time"] / 60
    ).round(2)

    # ---------------------------------------------------------
    # Calculate total trip value
    # ---------------------------------------------------------

    df["total_revenue"] = (
        df["base_passenger_fare"].fillna(0)
        + df["tolls"].fillna(0)
        + df["bcf"].fillna(0)
        + df["sales_tax"].fillna(0)
        + df["congestion_surcharge"].fillna(0)
        + df["airport_fee"].fillna(0)
        + df["tips"].fillna(0)
    ).round(2)

    # ---------------------------------------------------------
    # Rename API location columns
    # ---------------------------------------------------------

    df = df.rename(
        columns={
            "pulocationid": "pickup_location",
            "dolocationid": "dropoff_location"
        }
    )

    # ---------------------------------------------------------
    # Select final warehouse columns
    # ---------------------------------------------------------

    df = df[
        [
            "hvfhs_license_num",
            "dispatching_base_num",
            "originating_base_num",

            "request_datetime",
            "on_scene_datetime",
            "pickup_datetime",
            "dropoff_datetime",

            "pickup_date",
            "dropoff_date",
            "pickup_hour",
            "pickup_day",

            "pickup_location",
            "dropoff_location",

            "trip_miles",
            "trip_time",
            "trip_duration_minutes",

            "base_passenger_fare",
            "tolls",
            "bcf",
            "sales_tax",
            "congestion_surcharge",
            "airport_fee",
            "tips",
            "driver_pay",

            "total_revenue",

            "shared_request_flag",
            "shared_match_flag",
            "wav_request_flag",
            "wav_match_flag"
        ]
    ]

    # ---------------------------------------------------------
    # Remove invalid records
    # ---------------------------------------------------------

    df = df[
        (df["trip_miles"] >= 0) &
        (df["trip_time"] >= 0) &
        (df["base_passenger_fare"] >= 0)
    ]

    # ---------------------------------------------------------
    # Reset index
    # ---------------------------------------------------------

    df = df.reset_index(drop=True)

    # ---------------------------------------------------------
    # Logging
    # ---------------------------------------------------------

    logger.info(
        f"Rows After Transformation : {len(df)}"
    )

    print(
        f"Rows After Transformation : {len(df)}"
    )

    print("Transformation Successful")

    logger.info("Transform Phase Completed")

    return df