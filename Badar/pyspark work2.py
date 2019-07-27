# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 10:08:54 2019

@author: Owner
"""

from pyspark import SparkContext
sc = SparkContext("local", "Collect app")
words = sc.parallelize (
   ["scala", 
   "java", 
   "hadoop", 
   "spark", 
   "akka",
   "spark vs hadoop", 
   "pyspark",
   "pyspark and spark"]
)
coll = words.collect()
print ("Elements in RDD -> %s" % (coll))
