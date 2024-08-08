"""
你想匹配或者搜索特定模式的文本
比如 str.find() , str.endswith() , str.startswith()
"""
import re

text = 'yeah, but no, but yeah, but no, but yeah'
print(text.startswith('yeah'))
print(text.endswith("yea"))
print(text.find('no'))
# 对于复杂的匹配需要使用正则表达式和 re 模块
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')

# 使用同一个模式去做多次匹配，你应该先将模式字符串预编译为模式对象
datepat = re.compile(r'\d+/\d+/\d+')
# match() 总是从字符串开始去匹配 findall() 方法
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat.findall(text)
# 捕获分组
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datepat.match('11/27/2012')
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))

