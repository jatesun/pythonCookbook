"""
代理模式
代理是一种编程模式，它将某个操作转移给另外一个对象来实现。
"""


class A:
    def spam(self, x):
        print("a-spam")
        pass

    def foo(self):
        pass


class B1:
    def __init__(self):
        self._a = A()

    def spam(self, x):
        return self._a.spam(x)

    def foo(self):
        return self._a.foo()

    def bar(self):
        pass

    # 大量方法需要代理,使用getattr


class B2:
    def __init__(self):
        self._a = A()

    def bar(self):
        pass

    def __getattr__(self, name):
        return getattr(self._a, name)


b = B2()
print(b.spam(3))
