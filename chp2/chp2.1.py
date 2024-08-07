"""
你需要将一个字符串分割为多个字段，但是分隔符(还有周围的空格)并不是固定的。
需要更加灵活的切割字符串的时候，最好使用 re.split() 方法
"""
import re

line = 'asdf fjdk; afed, fjek,asdf, foo'
result = re.split(r'[;,\s]\s*', line)
print(result)
