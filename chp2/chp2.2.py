"""
你需要通过指定的文本模式去检查字符串的开头或者结尾，比如文件名后缀，URL Scheme等等。
"""
import os

filename = 'spam.txt'
result = filename.endswith('txt')
print(result)
# 如果你想检查多种匹配可能，只需要将所有的匹配项放入到一个元组中去
filenames = os.listdir('.')
print(filenames)
result = [name for name in filenames if name.endswith(('.py', '.py1'))]
print(result)
result1 = any(name.endswith('.py') for name in filenames)
print(result1)
