"""
你想创建或测试正无穷、负无穷或NaN(非数字)的浮点数。
但是可以使用 float() 来创建它们
"""
import math

a = float('inf')
b = float('-inf')
c = float('nan')
print(a)
print(b)
print(c)
print(math.isinf(a))
