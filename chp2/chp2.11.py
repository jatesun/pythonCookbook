"""
你想去掉文本字符串开头，结尾或者中间不想要的字符，比如空白。
strip() 方法能用于删除开始或结尾的字符。 lstrip() 和 rstrip() 分别从左和从右执行删除操作。 默认情况下，这些方法会去除空白字符，但是你也可以指定其他字符
"""
s = ' hello world \n'
# print(s.strip())
print(s.lstrip())
