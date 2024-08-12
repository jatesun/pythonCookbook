"""
你需要对浮点数执行精确的计算操作，并且不希望有任何小误差的出现。
浮点数的一个普遍问题是它们并不能精确的表示十进制数,可以使用decimal
"""
# print(4.2 + 2.1)  # 这是因为计算机使用的为2进制，而我们日常使用的是十进制。
# decimal模块
from decimal import Decimal

a = Decimal('4.2')
b = Decimal('2.1')
print(a + b)
# 数字位数和四舍五入运算。
from decimal import localcontext

a = Decimal('1.3')
b = Decimal('1.7')
print(a / b)
with localcontext() as ctx:
    # ctx.prec = 3
    ctx.prec = 50
    print(a / b)
