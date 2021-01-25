# 开发者：Lingyu
# 开发时间：2021/1/25 23:25
import pandas as pd
import numpy as np
d1 = [{'name': 'wenge', 'age': 25, 'gender': 'female'}, {'name': 'haha', 'gender': 'male'}, {'name':'hehe', 'age': 27}]
t1 = pd.DataFrame(d1)
print(t1, type(t1))
print('*'*50)
print(t1.index)  # 行索引
print('*'*50)
print(t1.columns) # 列索引
print('*'*50)
print(t1.values, type(t1.values))  # 值
print('*'*50)
print(t1.shape) # 形状，几行几列
print('*'*50)
print(t1.dtypes) # 类型
print('*'*50)
print(t1.ndim) # 维度
print('*'*50)
print(t1.head(2)) # 显示头几行，默认5行
print('*'*50)
print(t1.tail(2)) # 显示后几行，默认5行
print('*'*50)
print(t1.info()) # 显示行数，列数，行索引，列索引，列非空值个数，列类型，内存占用
print('*'*50)
print(t1.describe()) # 显示平均值，标准差，最大值，最小值，四分位数，个数
print('*'*50)

# 举例练习
t2 = pd.read_csv('F:/Pycharm/基础知识学习/Pandas/Pandas_shuju_lianxi.csv')
print('t2',t2)
print('*'*50)
print(t2.head())
print('*'*50)
print(t2.info())
print('*'*50)

