from pyspark.sql import SparkSession

# # Replace these values with your Spark master URL and ADLS connection details
# spark_master_url = "spark://spark-master:7077"
# adls_account_name = "nimbussstorageaccounnt"
# adls_account_key = "VKT5Zk+JLdB+19Mg9REV9551DUrFc8SWtPbOu1Ww4L295G0W2regfK8uWoyMgmewIsHIukafpvG9+AStpN8t3g=="
# file_system_name = "your_file_system"
# directory_name = "your_directory"
connection_string = 'DefaultEndpointsProtocol=https;AccountName=nimbussstorageaccounnt;AccountKey=VKT5Zk+JLdB+19Mg9REV9551DUrFc8SWtPbOu1Ww4L295G0W2regfK8uWoyMgmewIsHIukafpvG9+AStpN8t3g==;EndpointSuffix=core.windows.net'

# # Create a Spark session
# spark = SparkSession.builder \
#     .appName("DataTransformation") \
#     .master(spark_master_url) \
#     .getOrCreate()

# # Load data from ADLS
# adls_file_path = f"adl://{file_system_name}.azuredatalakestore.net/{directory_name}/your_data.csv"
# df = spark.read.csv(adls_file_path, header=True, inferSchema=True)

# df.head()

# # Stop the Spark session
# spark.stop()
from azure.storage.filedatalake import DataLakeServiceClient

service = DataLakeServiceClient.from_connection_string(conn_str=connection_string)
result = service.list_file_systems()

for res in result:
    print(res.name)
print(result)