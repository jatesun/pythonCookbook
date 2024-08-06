"""
如果你的程序包含了大量无法直视的硬编码切片，并且你想清理一下代码。
"""
# 假定你要从一个记录（比如文件或其他类似格式）中的某些固定位置提取字段
######    0123456789012345678901234567890123456789012345678901234567890'
record = '....................100 .......513.25 ..........'
cost = int(record[20:23]) * float(record[31:37])
print(cost)
# 与其那样写，为什么不像这样命名切片呢：
SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])  # 意义明确代码更加清晰可读
print(cost)
###### 讨论
items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[2:4])
print(items[a])
items[a] = [10, 11]
print(items)
del items[a]
print(items)
