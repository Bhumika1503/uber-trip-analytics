from config.logger import logger


def validate(df):

    logger.info("Validation Started")

    print("Running Validation...")

    if df.empty:
        raise Exception("Dataset is Empty!")

    if df.isnull().all().all():
        raise Exception("Dataset contains only NULL values!")

    print("Validation Successful")

    logger.info("Validation Successful")

    return df