# DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow import DAG
from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow.hooks.mysql_hook import MySqlHook
from airflow.models import Variable
from datetime import timedelta, date
from airflow.operators.dummy_operator import DummyOperator


# Initial block
filename = '/opt/airflow/dags/repo/dags/ruby/update_marketing_mysql.sql'

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

def run_sql_in_db():
    query = read_sql(filename)
    db_hook = MySqlHook("ghetto")
    db_hook.run(query)

update_marketing_account_data = PythonOperator(
    task_id="run_sql_in_db",
    python_callable= run_sql_in_db,
    dag=dag
)

start_task = DummyOperator(task_id="start_task", dag=dag)

start_task >> update_marketing_account_data

