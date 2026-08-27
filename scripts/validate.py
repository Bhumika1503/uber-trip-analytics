from config.logger import logger


REQUIRED_COLUMNS = [
    "hvfhs_license_num",
    "pickup_datetime",
    "dropoff_datetime",
    "pulocationid",
    "dolocationid",
    "trip_miles",
    "trip_time",
    "base_passenger_fare",
    "tips",
    "driver_pay"
]


def validate(df):

    logger.info("Validation Phase Started")

    print("Running Validation...")

    # Check if data exists
    if df is None or df.empty:
        raise ValueError("No data received from source.")

    # Check required columns
    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    # Check Uber records
    if not (df["hvfhs_license_num"] == "HV0003").all():
        raise ValueError(
            "Dataset contains non-Uber records."
        )

    # Check duplicate rows
    duplicate_count = df.duplicated().sum()

    if duplicate_count > 0:

        logger.warning(
            f"Duplicate rows found: {duplicate_count}"
        )

        print(
            f"Warning: {duplicate_count} duplicate rows found."
        )

    # Check important numeric fields
    numeric_columns = [
        "trip_miles",
        "trip_time",
        "base_passenger_fare",
        "tips",
        "driver_pay"
    ]

    for column in numeric_columns:

        df[column] = __import__("pandas").to_numeric(
            df[column],
            errors="coerce"
        )

    # Check missing values in critical fields
    critical_columns = [
        "pickup_datetime",
        "dropoff_datetime",
        "trip_miles",
        "trip_time"
    ]

    for column in critical_columns:

        if df[column].isna().any():

            logger.warning(
                f"Missing values found in {column}"
            )

    print("Validation Successful")

    logger.info("Validation Phase Completed")

    return df