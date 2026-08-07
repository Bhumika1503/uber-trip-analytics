from pyspark.sql import SparkSession

def get_spark():

    spark = (
        SparkSession.builder
        .appName("Uber Analytics")
        .master("local[*]")
        .getOrCreate()
    )

    return spark