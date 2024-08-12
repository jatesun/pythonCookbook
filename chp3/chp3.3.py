"""
你需要将数字格式化后输出，并控制数字的位数、对齐、千位分隔符和其他的细节。
格式化输出单个数字的时候，可以使用内置的 format() 函数
"""
x = 1234.56789
print(format(x, '0.2f'))
print(format(x, '>10.1f'))
print(format(x, '<10.1f'))
print(format(x, '^10.1f'))
print(format(x, ','))  # 千分位格式化
print(format(x, '0,.1f'))
# 指数
print(format(x, 'e'))
print(format(x, '0.2E'))
