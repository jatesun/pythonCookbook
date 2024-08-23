"""
你想读写二进制文件，比如图片，声音文件等等。
使用模式为 rb 或 wb 的 open() 函数来读取或写入二进制数据。
"""
with open('somefile.bin', 'rb') as f:
    data = f.read()
    # text = data.decode('utf-8') 如果要转为字符串，要解码

with open('somefile.bin', 'wb') as f:
    f.write(b'Hello World')
# 索引和迭代动作返回的是字节的值而不是字节字符串
t = 'Hello World'
print(t[0])
s = b'Hello World'
print((s[0]))