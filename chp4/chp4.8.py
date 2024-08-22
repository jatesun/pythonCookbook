"""
你想遍历一个可迭代对象，但是它开始的某些元素你并不感兴趣，想跳过它们。
itertools 模块中有一些函数可以完成这个任务。 首先介绍的是 itertools.dropwhile() 函数。
"""
from itertools import dropwhile

with open('etc/passwd') as f:
    for line in f:
        print(line)

with open('etc/passwd') as f:
    for line in dropwhile(lambda line: not line.startswith('#'), f):
        print(line, end='')
