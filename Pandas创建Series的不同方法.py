# 开发者：Lingyu
# 开发时间：2021/1/23 18:59
import pandas as pd
import string

# 方法一：
t1 = pd.Series([1, 2, 24, 45, 24, 15], index=list('abcdef'))  # index为索引，要一一对应
print('t1:', t1)
print(type(t1))
print('*:' * 50)

# 方法二：
temp_dict = {'name': 'wenge', 'age': 25, 'tel': 17834574345}  # 冒号左边的为索引
t2 = pd.Series(temp_dict)
print(t2)   # 类型为object，表示内含字符串
print('*:' * 50)

# 方法三：字典推导式创建字典a
t3 = {string.ascii_uppercase[i]: i for i in range(12)}
t4 = pd.Series(t3)
print('t3:', t3)
print(type(t3))
print('*:' * 50)
print('t4:', t4)
print(type(t4))
print('*:' * 50)
t5 = pd.Series(t3, index=list(string.ascii_uppercase[5:17]))  # 给t3重新指定索引
print('t5:', t5)
print(type(t5))
print('*:' * 50)  # naN为float

# 修改Series类型,与Numpy操作相同
t4 = t4.astype(float)
print(t4)