from pathlib import Path
from pyspark.sql import SparkSession


def get_spark():

    project_root = Path(__file__).resolve().parent.parent

    postgres_jar = (
        project_root
        / "drivers"
        / "postgresql-42.7.13.jar"
    )

    spark = (
        SparkSession.builder
        .appName("Uber Trip Analytics")
        .master("local[*]")
        .config("spark.jars", str(postgres_jar))
        .getOrCreate()
    )

    return spark