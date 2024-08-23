"""
你需要读写各种不同编码的文本数据，比如ASCII，UTF-8或UTF-16编码等。
使用带有 rt 模式的 open() 函数读取文本文件
"""
with open('somefile.txt', 'rt') as f:
    data = f.read()

with open('somefile.txt', 'rt') as f:
    for line in f:
        pass

# 写入一个文本文件，使用带有 wt 模式的 open() 函数
# Write chunks of text data
with open('somefile.txt', 'wt') as f:
    f.write('')
    f.write('')
    ...

# Redirected print statement
with open('somefile.txt', 'wt') as f:
    print('', file=f)
    print('line2', file=f)
    ...
