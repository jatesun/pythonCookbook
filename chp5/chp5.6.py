"""
你想使用操作类文件对象的程序来操作文本或二进制字符串。
使用 io.StringIO() 和 io.BytesIO() 类来创建类文件对象操作字符串数据
"""
import io

s = io.StringIO()
print(s.write('hello\n'))
print(s.getvalue())
# io.StringIO 只能用于文本如果你要操作二进制数据，要使用 io.BytesIO 类来代替