from pyspark.sql import SparkSession

adls_account_name = "nimbussstorageaccounnt"
adls_account_key = "VKT5Zk+JLdB+19Mg9REV9551DUrFc8SWtPbOu1Ww4L295G0W2regfK8uWoyMgmewIsHIukafpvG9+AStpN8t3g=="
input_folder = 'inputs'
container = 'nimbus-data-lake'

spark = SparkSession.builder.appName("testing_spark") \
        .config('spark.jars.packages', 'org.apache.hadoop:hadoop-azure-3.3.6.jar') \
        .config('spark.jars.packages', 'org.apache.hadoop:azure-storage-java-9.8.1.jar') \
        .config("fs.azure.account.key."+adls_account_name+".dfs.core.windows.net", adls_account_key) \
        .getOrCreate()

og_file_location = f"abfss://{container}@{adls_account_name}.dfs.core.windows.net/{input_folder}/OWNERSHIP_OG_DATA.csv"

og_local_path = "OWNERSHIP OG DATA.csv"

og_df = spark.read\
  .format("csv") \
  .option("inferSchema", "true") \
  .option("header", "true") \
  .load(og_file_location)


print(og_df.show(6))

spark.stop()