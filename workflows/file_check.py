from airflow import DAG
from datetime import datetime,timedelta
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor

default_argu={
	"owner":"airflow",
	"depends_on_past":False,
	"start_date":datetime(2026,8,17),
	"email":["airflow@airflow.com"],
	"email_on_failure":False,
	"email_on_retry":False,
	"retries":1,
	"retry_delay":timedelta(minutes=5),
}

dag=DAG("file_sensor",default_args=default_argu,schedule=timedelta(1))


f1 = FileSensor(task_id="file1",filepath="s3://airflowbucket1810/dags/branchcode.py",fs_conn_id="file_conn",poke_interval=10,timeout=100,dag=dag )
t1 = BashOperator(task_id="print_date",bash_command="date",dag=dag)
f1>>t1