import pandas as pd
from config.logger import logger


def extract():

    logger.info("Extract Phase Started")

    print("Reading Parquet File...")

    df = pd.read_parquet("data/raw/yellow_tripdata_2023-01.parquet")

    logger.info(f"Rows Extracted : {len(df)}")

    print(f"Rows Extracted : {len(df)}")

    return df