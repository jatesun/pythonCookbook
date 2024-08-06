"""
过滤序列元素
你有一个数据序列，想利用一些规则从中提取出需要的值或者是缩短序列
"""
import math

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
list1 = [n for n in mylist if n > 0]
list2 = [n for n in mylist if n < 0]
print(list1)
print(list2)

# 如果你对内存比较敏感，那么你可以使用生成器表达式迭代产生过滤的元素
pos = (n for n in mylist if n > 0)
for x in pos:
    print(x)

# filter() 函数
values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int, values))  # filter
print(ivals)

# 过滤的时候转换数据
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
list3 = [math.sqrt(n) for n in mylist if n > 0]
print(list3)

# 将不符合条件的值用新的值代替，而不是丢弃它们
clip_neg = [n if n > 0 else 0 for n in mylist]
