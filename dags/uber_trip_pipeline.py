from datetime import datetime

from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

PROJECT_DIR = "/mnt/d/projects/uber-trip-analytics"
VENV_PYTHON = "/home/shubh/airflow-project/venv/bin/python"

with DAG(
    dag_id="uber_trip_pipeline",
    start_date=datetime(2026, 8, 1),
    schedule=None,
    catchup=False,
    tags=["uber", "data-engineering"],
) as dag:

    run_etl = BashOperator(
        task_id="run_etl_pipeline",
        bash_command=f"cd {PROJECT_DIR} && {VENV_PYTHON} main.py",
    )

    run_spark = BashOperator(
        task_id="run_spark_analytics",
        bash_command=(
            f"cd {PROJECT_DIR} && "
            f"PYTHONPATH={PROJECT_DIR} "
            f"{VENV_PYTHON} -m spark.main"
        ),
    )

    run_etl >> run_spark