"""
你想实现一个自定义迭代模式，跟普通的内置函数比如 range() , reversed() 不一样。
"""


def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


for n in frange(0, 4, 0.5):
    print(n)

print(list(frange(0, 1, 0.125)))


# 一个函数中需要有一个 yield 语句即可将其转换为一个生成器。  跟普通函数不同的是，生成器只能用于迭代操作

def countdown(n):
    print('start count from', n)
    while n > 0:
        yield n
        n -= 1
    print('done')


c = countdown(3)
next(c)
next(c)
next(c)
next(c)
