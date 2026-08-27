import requests
import pandas as pd

from config.logger import logger


API_URL = "https://data.cityofnewyork.us/resource/u253-aew4.json"

MAX_ROWS = 500


def extract():

    logger.info("Extract Phase Started")

    print("Fetching Uber trip data from NYC Open Data API...")

    params = {
        "$where": "hvfhs_license_num = 'HV0003'",
        "$limit": MAX_ROWS
    }

    response = requests.get(
        API_URL,
        params=params,
        timeout=60
    )

    response.raise_for_status()

    data = response.json()

    df = pd.DataFrame(data)

    print(f"Rows Extracted : {len(df)}")

    logger.info(
        f"Rows Extracted : {len(df)}"
    )

    return df