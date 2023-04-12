# DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow import DAG
from airflow.models import Variable
from datetime import timedelta, date
from airflow.operators.dummy_operator import DummyOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryExecuteQueryOperator


# Initial block
filename = '/opt/airflow/dags/repo/dags/ruby/update_marketing_bigquery.sql'

# Dag Initial
default_args = {
    'owner': 'rubenchik',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
	'execution_timeout': timedelta(hours=1)
    }

dag = DAG(
    "mart_data.marketing_account",
    description="Update marketing account data for the last 30 days",
    schedule_interval="0 3 * * *",
    start_date=datetime(2022, 10, 15),
    catchup=False,
    default_args=default_args,
	tags=["marketing", "update", "leads"],
)

#Function and operators

def read_sql(filename):
    f = open(filename, "r")
    text = ""
    while True:
        line = f.readline()
        if not line:
            break
        text = text + line
    return text

sql = read_sql(filename)

start_task = DummyOperator(task_id="start_task", dag=dag)

update_marketing_account_data = BigQueryExecuteQueryOperator(
    task_id="update_marketing_account_data",
    sql=sql,
    use_legacy_sql=False,
    dag=dag,
)

start_task = DummyOperator(task_id="start_task", dag=dag)

start_task >> update_marketing_account_data

