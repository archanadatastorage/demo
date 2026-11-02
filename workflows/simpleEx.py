
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(
    dag_id="simple_empty_example",
    start_date=datetime(2026, 10, 1),
    schedule=None,
    catchup=False
) as dag:

    start = EmptyOperator(
        task_id="start"
    )

    process_data = EmptyOperator(
        task_id="process_data"
    )

    end = EmptyOperator(
        task_id="end"
    )

start >>  [process_data ,end]