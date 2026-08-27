from config.database import engine
from config.logger import logger


def load(df):

    logger.info("Load Phase Started")

    print("Loading data into PostgreSQL...")
    print("Columns being loaded:")
    print(df.columns.tolist())

    try:

        df.to_sql(
            name="fact_trips",
            con=engine,
            schema="warehouse",
            if_exists="append",
            index=False,
            method="multi"
        )

        print(f"Rows Loaded : {len(df)}")

        logger.info(
            f"Rows Loaded : {len(df)}"
        )

        print("Load Phase Completed")

        return df

    except Exception as e:

        logger.exception("Load Phase Failed")

        print(f"Load Failed: {e}")

        raise