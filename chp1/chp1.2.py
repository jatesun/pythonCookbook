"""
Q:如果一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError 。 那么怎样才能从这个可迭代对象中解压出 N 个元素出来？
A:Python 的星号表达式可以用来解决这个问题(去掉最高、最低分，取中间值平均值)
"""
import numpy as np


def drop_first_last(grades):
    first, *middle, last = grades
    return np.mean(middle)


grades = (88, 93, 98, 83, 98, 84, 74, 85, 80, 94)
print(drop_first_last(grades))

"""
用户的记录列表，每条记录包含一个名字、邮件，接着就是不确定数量的电话号码
"""
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone = record
print(name)
print(email)
print(phone)

"""
最近一个月数据和前面 7 个月的平均值
"""
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(np.mean(trailing))
print(current)

"""
可变元组序列
"""
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

"""
你想解压一些元素后丢弃它们，你不能简单就使用 * ， 但是你可以使用一个普通的废弃名称，比如 _ 或者 ign （ignore）。
"""
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
print(year)
