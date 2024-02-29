from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'Emmanuel',
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

with DAG(
    dag_id='connect_load_data_etl',
    default_args=default_args,
    start_date=datetime(2023, 10, 2),
    schedule_interval='@once',
    tags=['testing', 'spark']
) as dag:
        
    start_workflow = DummyOperator(task_id='start')

    spark_job = SparkSubmitOperator(
        task_id='spark_job',
        conn_id='spark-conn',
        application='jobs/test_word_count.py',
        packages="org.apache.hadoop:hadoop-client-runtime:3.3.6",
        # org.apache.hadoop:hadoop-azure:3.0.1,org.apache.hadoop:hadoop-common:3.0.1,org.apache.hadoop:hadoop-annotations:3.0.1,org.apache.hadoop:hadoop-auth:3.0.1,
        repositories="https://repo1.maven.org/maven2/",
        conf={"spark.executor.extraClassPath": "/opt/bitnami/spark/jars",
              "spark.executor.extraClassPath": "/opt/bitnami/spark/jars"},

    )

    end_workflow = DummyOperator(task_id='end')

    start_workflow >> spark_job >> end_workflow