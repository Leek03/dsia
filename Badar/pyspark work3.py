# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 10:34:24 2019

@author: Owner
"""
from pyspark.sql import Row
from pyspark.sql import SparkSession
from pyspark.sql.types import *

spark = SparkSession.builder.appName("Python Spark SQL basic example").config("spark.some.config.option", "some-value").getOrCreate()

sc = spark.sparkContext
lines = sc.textFile("people.txt")
parts = lines.map(lambda l: l.split(","))
people = parts.map(lambda p: Row(name=p[0],age=int(p[1])))
peopledf = spark.createDataFrame(people)
# Specify Schema
people = parts.map(lambda p: Row(name=p[0],
age=int(p[1].strip())))
schemaString = "name age"
fields = [StructField(field_name, StringType(), True) for field_name in schemaString.split()]
schema = StructType(fields)
spark.createDataFrame(people, schema).show()