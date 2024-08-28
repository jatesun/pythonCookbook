"""
函数的某些参数强制使用关键字参数传递
"""


def recv(maxsize, *, block):
    'Receives a message'
    pass


recv(1024, True)  # TypeError
recv(1024, block=True)  # 必须使用参数

# 很多情况下，使用强制关键字参数会比使用位置参数表意更加清晰，程序也更加具有可读性。
