"""
你想得到一个由迭代器生成的切片对象，但是标准切片操作并不能做到。
"""


def count(n):
    while True:
        yield n
        n += 1


c = count(0)
# print(c[10:20])
import itertools

for x in itertools.islice(c, 10, 20):
    print(x)
