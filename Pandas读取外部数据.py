# 开发者：Lingyu
# 开发时间：2021/1/24 23:14
from pymongo import MongoClient
import pandas as pd
# pandas读取.csv中的文件
df = pd.read_csv('F:/Pycharm/基础知识学习/Pandas/Pandas_shuju_lianxi.csv')
print(df)
print(type(df))

# Pandas读取mysql数据库中的数据
# pd.read_sql(sql_sentence, connection)

# Pandas读取mongodb数据库中的数据    没弄懂
client = MogoClient()
collection = client['douban']['tv1']
data = list(collection.find())
print(data)
