# AWS S3 Bucket data upload
A system that uploads data everyday at 8pm KST to the S3 bucket. Implemented airflow for the automation and slack alert incase of an error or downtime 


## Table of Contents: Folders Code distribution

- [Main](#Main)
- [Structure](#Structure)
- [Airflow](#Airflow)
- [Logs](#log)
- [Utils](#Utils)



## Main
<details><summary>main.py</summary>
run python3 main.py to run all script and send result to the S3 bucket. 
</details>

## Structure
<details><summary>Folder structure</summary>

```
S3Backupdata/
│
├── Airflow/
│   └── dags
        └── run_task.py
    └── logs
│
├── logs/
│   └── log_config.py
    └── logs.py
│
├── Utils/
│   └── slack_alart.py
└── main.py

```
</details>

## Airflow
<details>
<summary>Dags</summary>
<b>Important File:</b> run_task.py
This Apache Airflow DAG, named "s3_upload," is designed for scheduling a task related to uploading data to an S3 bucket. The DAG is configured with several parameters to control its behavior and includes a task that executes a Python script for S3 data backup.

# DAG: s3_upload

This Apache Airflow DAG, named "s3_upload," is designed for scheduling a task related to uploading data to an S3 bucket. The DAG is configured with several parameters to control its behavior and includes a task that executes a Python script for S3 data backup.

## Important Parameters and Components:

### 1. `from __future__ import annotations`:
   - Enables postponed evaluation of type annotations, allowing forward references in type hints.

### 2. DAG Initialization:
   - `dag_id`: Unique identifier for the DAG.
   - `schedule`: The DAG runs daily at 00:20, specified using a cron-like expression.
   - `default_args`: Dictionary containing default parameters for the DAG.
   - `start_date`: The date and time when the DAG should start running.
   - `catchup`: If set to `False`, the DAG will only run for the latest interval.
   - `dagrun_timeout`: Maximum allowed execution time for DAG runs.
   - `tags`: List of tags associated with the DAG.
   - `on_success_callback` and `on_failure_callback`: Callback functions to be executed on DAG success and failure, respectively.

### 3. `SlackAlert` Initialization:
   - An instance of the `SlackAlert` class is created with a Slack channel and an empty Slack token. The `SlackAlert` class is presumably designed to send alerts to a Slack channel for different events.

### 4. Task Initialization (`BashOperator`):
   - A task named `s3_upload` is created using the `BashOperator`.
   - The task runs a bash command to execute a Python script (`main.py`) related to S3 data backup. The script is executed with sudo privileges as the "ubuntu" user.
   - This task is associated with the DAG (`dag=dag`).

### 5. Main Execution Block:
   - The `if __name__ == "__main__":` block allows the DAG to be run manually from the command line using the `dag.cli()` method.

</details> 
        
## Logs
<details>
<summary>logging folder</summary>
File: log.py, log_config.py.py

The LoggerManager class facilitates logging in Python applications. Instantiate it, then use its info, debug, or error methods to log messages at different levels. Log files are stored in the 'Logs' directory with date-stamped filenames.

# Instantiate the LoggerManager
logger_manager = LoggerManager()

# Log an info message
logger_manager.info("This is an info message.")

# Log a debug message
logger_manager.debug("This is a debug message.")

# Log an error message with filename and line number
logger_manager.error("This is an error message.", filename=__file__, line=10)

</details>

## Utils
<details>
<summary>Slack alert class</summary>

</details>

