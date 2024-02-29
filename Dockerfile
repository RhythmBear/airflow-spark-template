FROM apache/airflow:2.7.1-python3.11

USER root
RUN apt-get update && \
    sudo apt install procps -y && \
    apt-get install -y gcc python3-dev openjdk-11-jdk && \
    apt-get clean

# Set JAVA_HOME environment variable
ENV JAVA_HOME /usr

# Adjust permissions for the /opt/airflow directory
RUN chown -R airflow: /opt/airflow

USER airflow


RUN pip install apache-airflow apache-airflow-providers-apache-spark apache-airflow-providers-microsoft-azure pyspark