"""
定义接口或者抽象基类
使用 abc 模块可以很轻松的定义抽象基类
"""
from abc import ABCMeta, abstractmethod


class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


class SocketStream(IStream):
    def read(self, maxbytes=-1):
        print("socket read")

    def write(self, data):
        print("socket write")


IStream = SocketStream()
print(IStream.read())
