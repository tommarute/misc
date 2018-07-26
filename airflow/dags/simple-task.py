import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'tommarute',
    'depends_on_past': False,
    'start_date': airflow.utils.dates.days_ago(0),
    'email': ['tommarute@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'simple-task',
    default_args=default_args,
    description='A simple task of DAG',
    schedule_interval='*/10 * * * *',
    catchup=False
    )

t1 = BashOperator(
    task_id='print_date',
    bash_command='date >> /tmp/date.log 2>&1',
    dag=dag
    )
