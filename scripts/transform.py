from config.logger import logger


def transform(df):

    logger.info("Transformation Started")

    print("Transforming Data...")

    df["trip_duration"] = (
        df["tpep_dropoff_datetime"] -
        df["tpep_pickup_datetime"]
    ).dt.total_seconds() / 60

    df["pickup_hour"] = (
        df["tpep_pickup_datetime"].dt.hour
    )

    logger.info("Transformation Completed")

    print("Transformation Completed")

    return df