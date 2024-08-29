"""
你想在子类中调用父类的某个已经被覆盖的方法。
"""


class A:
    def __init__(self):
        self.x = 0

    def spam(self):
        print("a.spam")


class B(A):
    def __init__(self):
        super().__init__()
        self.y = 1

    def spam(self):
        # print("b.spam")
        super().spam()


b = B()
b.spam()

# super() 函数的一个常见用法是在 __init__() 方法中确保父类被正确的初始化了：
