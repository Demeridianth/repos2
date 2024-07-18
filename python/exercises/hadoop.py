from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
import pyspark.sql.functions as func

spark = SparkSession.builder.appName("SparkSQL").getOrCreate()

# True means Nullable (can contain NUll values)
myschema = StructType([\
                       StructField("userID", IntegerType(), True), 
                       StructField("item", StringType(), True),
                       StructField("name",StringType(), True),
                       StructField("size",IntegerType(), True),
                       StructField("location",IntegerType(), True),
                       StructField("height",IntegerType(), True),
                       StructField("width",IntegerType(), True),
                       StructField("nunavut",StringType(), True),
                       StructField("type",StringType(), True),
                       StructField("speed",IntegerType(), True),
                        ])


people = spark.read.format("csv")\
    .schema(myschema)\
    .option("path","hdfs:///user/maria_dev/spark/items.csv")\
    .load()

people.printSchema()

# withColumn adds new column 'inser_ts' and using current timestamp func
output = people.select(people.userID, people.item, people.name, people.size, people.location , people.height, people.width)\
         .withColumn('insert_ts', func.current_timestamp())\
         .orderBy(people.userID).cache()
# cache stores the dataframe in memory

# creates temporary view for the console
output.createOrReplaceTempView("all_items")

# what would be displayed on the console
spark.sql("select userID, name from peoples where size > 2 order by userID").show()

output.write\
.format("json").mode("overwrite")\
.option("path", "hdfs:///user/maria_dev/spark/items_output/")\
.partitionBy("userID")\
.save()