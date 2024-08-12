"""
你有一个字节字符串并想将它解压成一个整数。或者，你需要将一个大整数转换为一个字节字符串。
使用 int.from_bytes() 方法
"""
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
print(len(data))
print(int.from_bytes(data, 'little'))  # 小端
print(int.from_bytes(data, 'big'))  # 大端
# 为了将一个大整数转换为一个字节字符串，使用 int.to_bytes() 方法
x = 94522842520747284487117727783387188
print(x.to_bytes(16, 'big'))
print(x.to_bytes(16, 'little'))
