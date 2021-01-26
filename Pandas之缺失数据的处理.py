# 开发者：Lingyu
# 开发时间：2021/1/26 16:17
import pandas as pd
import numpy as np
import string
t1 = pd.DataFrame(np.arange(12).reshape(3, 4), index=list('ABC'), columns=list('WXYZ'))
print('t1:', t1)
print('*'*50)
t1.loc['A', 'W'] = np.nan
t1.loc['B', 'Y'] = np.nan
t1.loc['C', 'X'] = np.nan
print('t1:', t1)
print('*'*50)
print(pd.isnull(t1))  # 布尔索引，是naN的为True
print('*'*50)
print(pd.notnull(t1))  # 布尔索引，不是naN的为True
print('*'*50)
print(t1[pd.notnull(t1['W'])])  # 选取t1中‘W’列不为naN所对应的行
print('*'*50)
print(t1.dropna(axis=1, how='all'))  # axis=1表示列，axis=0表示行，all表示只有某列全为naN才把该列去掉
print('*'*50)
print(t1.dropna(axis=1, how='any'))  # axis=1表示列，axis=0表示行，any表示某列只要有naN就把该列去掉
