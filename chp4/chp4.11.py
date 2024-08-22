"""
你想同时迭代多个序列，每次分别从一个序列中取一个元素。
"""
xpts = [1, 5, 4, 2, 10, 7]
ypts = [101, 78, 37, 15, 62, 99]
for x, y in zip(xpts, ypts):
    print(x, y)

# 当你想成对处理数据的时候 zip() 函数是很有用的。
headers = ['name', 'shares', 'price']
values = ['ACME', 100, 490.1]
s = dict(zip(headers, values))
