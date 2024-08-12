"""
你需要转换或者输出使用二进制，八进制或十六进制表示的整数。
二进制、八进制或十六进制的文本串， 可以分别使用 bin() , oct() 或 hex() 函数：
"""
x = 1234
print(bin(x))
print(oct(x))
print(hex(x))
# 不想输出 0b , 0o 或者 0x 的前缀的话，可以使用 format() 函数
print(format(x, 'b'))
print(format(x, 'o'))
print(format(x, 'x'))

# 不同进制转换字符串
print(int('4d2', 16))
