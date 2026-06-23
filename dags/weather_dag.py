import pandas as pd
from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime

import sys
sys.path.append(r"D:\Data\Data Engineering\ETL\Pipeline\scripts")


from extract import get_weather
from transform import transform_weather
from load import save_csv


def run_pipeline():

    raw = get_weather()

    transformed = transform_weather(raw)

    df = pd.DataFrame(transformed)
    df.to_csv(r"D:\Data\Data Engineering\ETL\data.csv")
    #save_csv(transformed)


with DAG(
    dag_id="weather_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule="@hourly",
    catchup=False,
) as dag:

    etl_task = PythonOperator(
        task_id="etl_task",
        python_callable=run_pipeline,
    )
