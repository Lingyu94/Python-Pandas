# 开发者：Lingyu
# 开发时间：2021/1/23 21:49
import pandas as pd
import string

# 切片：直接传入start end 或步长即可
# 索引：一个的时候直接传入序号或index，多个时传入序号或index列表
temp_dict = {'name': 'wenge', 'age': 25, 'tel': 17835643627}
t1 = pd.Series(temp_dict)
print('t1:', t1)
print(type(t1))
print('*' * 50)
print(t1['name'])
print(t1['age'])
print(t1[0])  # 取第一行
print(t1[1])  # 取第二行
print('*' * 50)
print(t1[:2])  # 取连续前二行
print('*' * 50)
print(t1[[0, 2]])  # 取第1行及第3行
print('*' * 50)
t2 = {string.ascii_uppercase[i]: i for i in range(10)}
t3 = pd.Series(t2)
print('t3:', t3)
print('*' * 50)
print(t3[t3 > 5])  # 布尔索引，取t3中值大于5的
print('*' * 50)

# 针对未知的Series类型，获取其索引及具体值
# 索引 index
temp_dict = {'name': 'wenge', 'age': 25, 'tel': 17835643627}
t4 = pd.Series(temp_dict)
print('t4:', t4)
print('*' * 50)
for i in t4.index:  # 可迭代
    print(i)
print('*' * 50)
print(t4.index)
print(type(t4.index))
print(len(t4.index))  # 长度
print(list(t4.index))  # 用list()转换成列表
print(type(list(t4.index)))
print(list(t4.index)[:2])  # 取前两行

# 值 values
print(t4.values)
print(type(t4.values))
print('*' * 50)

# pandas.where()的用法
t5 = pd.Series(range(5))
print('t5:', t5)
print(t5.where(t5 > 1))


