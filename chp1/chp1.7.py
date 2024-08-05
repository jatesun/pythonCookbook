"""
你想创建一个字典，并且在迭代或序列化这个字典的时候能够控制元素的顺序。
为了能控制一个字典中元素的顺序，你可以使用 collections 模块中的 OrderedDict 类。 在迭代操作的时候它会保持元素被插入时的顺序，示例如下：
"""
from collections import OrderedDict

d = OrderedDict()
# d = dict()
d['foo'] = 1
d['bar'] = 2
d['grok'] = 4
d['spam'] = 3
for key in d:
    print(key, d[key])
