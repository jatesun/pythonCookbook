"""
你写的最新的网络认证方案代码遇到了一个难题，并且你唯一的解决办法就是使用复数空间。 再或者是你仅仅需要使用复数来执行一些计算操作。
复数可以用使用函数 complex(real, imag) 或者是带有后缀j的浮点数来指定
"""
a = complex(2, 4)
b = 3 - 5j
print(a)
print(a + b)
print(str(a.real) + "," + str(a.imag) + "," + str(a.conjugate()))
