#!/usr/bin/env python



import findspark
findspark.init()
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("first code").master('local[3]').config('spark.driver.host','127.0.0.1')\
.config('spark.ui.port',0).getOrCreate()

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "first") \
    .load()

query = df.selectExpr(
    "CAST(key AS STRING)",
    "CAST(value AS STRING)"
).writeStream \
    .format("console") \
    .outputMode("append") \
    .option("truncate", "false") \
    .start()

query.awaitTermination()
