"""
你想在字符串中搜索和匹配指定的文本模式
 str.replace()
"""
import re

text = 'yeah, but no, but yeah, but no, but yeah'
result = text.replace('yeah', 'yep')
print(result)

# 对于复杂的模式，请使用 re 模块中的 sub() 函数
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

result = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(result)

# 如果你打算用相同的模式做多次替换，考虑先编译它来提升性能
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
datepat.sub(r'\3-\1-\2', text)
