import os

from dotenv import load_dotenv

from spark.session import get_spark


load_dotenv()


def read_uber_data():

    spark = get_spark()

    jdbc_url = (
        f"jdbc:postgresql://"
        f"{os.getenv('DB_HOST', 'localhost')}:"
        f"{os.getenv('DB_PORT', '5432')}/"
        f"{os.getenv('DB_NAME')}"
    )

    df = (
        spark.read
        .format("jdbc")
        .option("url", jdbc_url)
        .option("dbtable", "warehouse.fact_trips")
        .option("user", os.getenv("DB_USER"))
        .option("password", os.getenv("DB_PASSWORD"))
        .option("driver", "org.postgresql.Driver")
        .option("fetchsize", "1000")
        .load()
    )

    return df


if __name__ == "__main__":

    df = read_uber_data()

    print("Total Uber Trips:", df.count())

    df.printSchema()

    df.show(5, truncate=False)

    df.sparkSession.stop()