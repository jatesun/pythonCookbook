"""
你的程序要创建大量(可能上百万)的对象，导致占用很大的内存。
可以通过给类添加 __slots__ 属性来极大的减少实例所占的内存。
"""


class Date:
    __slots__ = ['year', 'month', 'day']

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

# 使用slots一个不好的地方就是我们不能再给实例添加新的属性了，只能使用在 __slots__ 中定义的那些属性名
