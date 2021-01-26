# 开发者：Lingyu
# 开发时间：2021/1/26 10:14
import pandas as pd
import numpy as np
import string

# DataFrame中排序的方法
t1 = pd.read_csv('F:/Pycharm/基础知识学习/Pandas/Pandas_shuju_lianxi.csv')
print('t1:', t1)
print('*'*50)
print(t1[t1['frequency'] > 5])  # 布尔索引，取频率大于5的部分
print('*'*50)
print(t1[(2 < t1['frequency']) & (t1['frequency'] < 15)])  # 选择‘frequency’大于2并且小于15的部分，，不同条件用（）括起来，&表示and
print('*'*50)
print(t1[(20 < t1['frequency']) | (t1['frequency'] < 5)])  # 选择‘frequency’大于20或小于5的部分，|表示或者
print('*'*50)
print(t1[(t1['name'].str.len() > 4) & (t1['frequency'] > 2)])  # 选择'name'字符串长度大于4并且‘frequency’大于2的部分
