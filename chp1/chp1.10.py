"""
怎样在一个序列上面保持元素顺序的同时消除重复的值？
"""


# hashable类型，那么可以很简单的利用集合或者生成器来解决这个问题。
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))


# 如果你想消除元素不可哈希（比如dict类型）的序列中重复元素的话，你需要将上述代码稍微改变一下
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


# 仅仅就是想消除重复元素，通常可以简单的构造一个集合,但是会打乱顺序，不打乱顺序参照上面
a = (1, 5, 2, 1, 9, 1, 5, 10)
print(set(a))
