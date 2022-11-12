c.InteractiveShellApp.exec_lines = [
    "from os import environ",
    "from subprocess import getoutput",
    "from pyspark import SparkConf",
    "from pyspark import SparkContext",
    "conf = SparkConf()",
    """conf.setMaster(environ['SPARK_MASTER_SVC_PORT_7077_TCP'].replace('tcp','spark'))""",
    """conf.set('spark.driver.host',getoutput('hostname -I').strip())""",
    "sc = SparkContext(conf=conf)"
]