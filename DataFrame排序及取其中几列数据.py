# 开发者：Lingyu
# 开发时间：2021/1/26 0:29
import pandas as pd
import numpy as np

# DataFrame中排序的方法
t1 = pd.read_csv('F:/Pycharm/基础知识学习/Pandas/Pandas_shuju_lianxi.csv')
t1 = t1.sort_values(by='frequency')  # 默认升序
print('t1',t1)
print('*'*50)
t1 = t1.sort_values(by='frequency', ascending=False) # False为降序
print('t1',t1)
print('*'*50)
print(t1.head(6))  # 取连续前6条记录，前6行
print('*'*50)