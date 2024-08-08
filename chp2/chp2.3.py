"""
你想使用 Unix Shell 中常用的通配符(比如 *.py , Dat[0-9]*.csv 等)去匹配文本字符串
解决方案
fnmatch 模块提供了两个函数—— fnmatch() 和 fnmatchcase() ，可以用来实现这样的匹配


"""
from fnmatch import fnmatch, fnmatchcase

print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
fnmatch('Dat45.csv', 'Dat[0-9]*')
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
result = [name for name in names if fnmatch(name, 'Dat*.csv')]
print(result)

# fnmatch() 函数使用底层操作系统的大小写敏感fnmatch('foo.txt', '*.TXT'),mac false,windows true
# 可以使用 fnmatchcase() 来代替
# fnmatch() 函数匹配能力介于简单的字符串方法和强大的正则表达式之间
