from session import get_spark

def read_data():

    spark = get_spark()

    df = spark.read.parquet(
        "data/raw/yellow_tripdata_2023-01.parquet"
    )

    return spark, df