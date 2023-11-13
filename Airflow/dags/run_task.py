from __future__ import annotations

from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow.utils.dates import days_ago
import datetime
import pendulum
from airflow.models.baseoperator import chain
from util.slack_alert import SlackAlert
import os

args = {
        'owner': 'admin'
}
ENV = os.getenv(endpoint)
slack = SlackAlert('#airflow-alarm', '')
##################################################



with DAG(
    dag_id = "s3_upload",
    schedule = '20 0 * * *',
    default_args=args,
    start_date = pendulum.datetime(2023, 9, 23, tz="Asia/Seoul"),
    catchup = False,
    dagrun_timeout = datetime.timedelta(minutes=600),
    tags = ["s3_upload"],
    on_success_callback=slack.send_success_alert,
    on_failure_callback=slack.send_fail_alert,
    # on_execute_callback=slack.send_alert
) as dag:


    s3_upload = BashOperator(
		task_id='s3bucket_upload',
			bash_command="sudo su - ubuntu -c 'python3 /S3Backupdata/main.py'",
			dag=dag,
	)

s3bucket_upload



if __name__ == "__main__":
		dag.cli()
