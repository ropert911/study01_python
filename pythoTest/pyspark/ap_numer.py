import sys
from collections import namedtuple
from pyspark.sql import SparkSession
from functools import reduce
import psycopg2

def main(para):
    print("ap_number.py:我已经启动")

    spark = get_and_conf_spark()

    print("ap_number.py:从hive中取数据")
    hive_sql = ('select day,datefmt,areaid,ap_base_mac from pm.ap_all where datefmt=2019030201')
    df = spark.sql(hive_sql)

    print("ap_number.py:RDD数据处理")
    Results = namedtuple('Result', ('datefmt','areaid', 'count'))
    gpresult = []
    results = df.rdd.groupBy(lambda x: x.areaid).collect()
    for areaid, values in results:
        gpresult.append(Results(2019030201,areaid, len(values)))
        print(" 区域：", areaid, " AP个数：", len(values))

    data = map(lambda s: [s.datefmt,s.areaid, s.count], gpresult)
    gp_sql = map(lambda s: '(' + ','.join(map(lambda d: str(d), s)) + ')', data)
    gp_sql = reduce(lambda a, b: a + ',' + b, gp_sql)

    gp_sql = 'INSERT INTO test_ap_numer VALUES {}'.format(gp_sql)
    print("ap_number.py:执行语句:" + gp_sql)

    try:
        conn = psycopg2.connect(host="192.168.20.48,192.168.20.47,192.168.20.49", dbname="pm", user="postgres", password='sks123.com',target_session_attrs="read-write")
        cursor = conn.cursor()
        cursor.execute(gp_sql)
        conn.commit()
    except Exception as e:
        print('postgres 失败(%s).' % e)

    spark.stop()
    print("ap_number.py:我已经退出")


def get_and_conf_spark() -> SparkSession:
    spark = SparkSession.builder.appName("Get_AP_NUMBER").enableHiveSupport().getOrCreate()
    spark.sparkContext.setLogLevel("INFO")
    spark.sql('set spark.sql.shuffle.partitions=%d' % 2)
    return spark


if __name__ == '__main__':
    main(sys.argv)
