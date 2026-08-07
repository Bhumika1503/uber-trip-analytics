import time

from scripts.extract import extract
from scripts.validate import validate
from scripts.transform import transform
from scripts.load import load
from scripts.database import database

from config.logger import logger


def main():

    start_time = time.time()

    print("=" * 60)
    print("UBER TRIP ANALYTICS PIPELINE")
    print("=" * 60)

    logger.info("Pipeline Started")

    try:

        df = extract()

        df = validate(df)

        df = transform(df)
        df = load(df)

        load(df)

        database()

        end_time = time.time()

        execution_time = round(end_time - start_time, 2)

        print(f"\nPipeline Completed Successfully!")

        print(f"Execution Time : {execution_time} seconds")

        logger.info(
            f"Pipeline Completed in {execution_time} seconds"
        )

    except Exception as e:

        print(f"\nPipeline Failed!")

        print(e)

        logger.exception(e)


if __name__ == "__main__":
    main()