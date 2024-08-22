"""
你想在迭代一个序列的同时跟踪正在被处理的元素索引。
"""
my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list):
    print(idx, val)


# 这种情况在你遍历文件时想在错误消息中使用行号定位时候非常有用：
def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = int(fields[1])
                ...
            except ValueError as e:
                print('Line {}: Parse error: {}'.format(lineno, e))
