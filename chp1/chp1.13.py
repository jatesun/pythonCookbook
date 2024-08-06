"""
你有一个字典列表，你想根据某个或某几个字典字段来排序这个列表。
通过使用 operator 模块的 itemgetter 函数，可以非常容易的排序这样的数据结构。 假设你从数据库中检索出来网站会员信息列表，并且以下列的数据结构返回：
"""
from operator import itemgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
rows_by_fname = sorted(rows, key=itemgetter('fname'))
print(rows_by_fname)
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_uid)
# itemgetter() 函数也支持多个 keys
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)
# lamda标识，但是使用 itemgetter() 方式会运行的稍微快点
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_lfname = sorted(rows, key=lambda r: (r['lname'], r['fname']))
# 同样适用于 min() 和 max() 等函数
print(min(rows, key=itemgetter('uid')))
print(max(rows, key=itemgetter('uid')))
