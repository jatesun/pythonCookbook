"""
将序列分解为单独的变量
任何的序列（或者是可迭代对象）可以通过一个简单的赋值操作来分解为单独的变量。 唯一的要求就是变量的总数和结构必须与序列相吻合。
不仅仅只是元组或列表，只要对象是可迭代的，就可以执行分解操作。 包括字符串，文件对象，迭代器和生成器。
"""
p = (4, 5)
x, y = p
# print(x)
# print(y)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
# name, shares, price, date = data
# print(name)
# print(shares)
# print(price)
# print(date)
# name, shares, price, (year, mon, day) = data
# print(name)
# print(shares)
# print(price)
# print(year)

# 不关心的数据可以占位符，然后忽略即可。
data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data
print(shares)
print(price)
