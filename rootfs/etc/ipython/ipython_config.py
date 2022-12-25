c.InteractiveShellApp.exec_lines = [
    """
from os import environ
from pyspark.sql import SparkSession
from subprocess import getoutput
from pyspark import SparkConf
from pyspark import SparkContext

for i in environ.keys():
    if len(i)-i.find("MASTER_SVC_PORT")==15 and environ[i].find("7077")>=0:
        master=environ[i].replace("tcp","spark")
        break

conf = SparkConf()
conf.setMaster(master)
conf.set('spark.driver.host',getoutput('hostname -I').strip())
conf.set('spark.jars.ivy',"./.ivy2")

try:
    if sc:
        sc.stop()
    if spark:
        spark.stop()
except:
    pass

sc=SparkContext(conf=conf)
spark = SparkSession(sc)
"""
]
