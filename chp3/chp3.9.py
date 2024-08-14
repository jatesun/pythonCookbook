"""
你需要在大数据集(比如数组或网格)上面执行计算。
可以使用 NumPy 库
"""
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
print(x * 2)
# print(x + 10)
print(x + y)
import numpy as np

ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])
print(ax * 2)
print(ax + 10)
print(ax + ay)
print(ax * ay)
# NumPy 还为数组操作提供了大量的通用函数，这些函数可以作为 math 模块中类似函数的替代
# 只要有可能的话尽量选择 NumPy 的数组方案。
grid = np.zeros(shape=(10000, 10000), dtype=float)  # 10000*10000的数组
print(grid)
grid += 10
np.sin(grid)
print(grid)