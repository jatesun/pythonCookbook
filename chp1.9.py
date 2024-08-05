"""
怎样在两个字典中寻寻找相同点（比如相同的键、相同的值等等）？

"""
a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

print(a.keys() & b.keys())
print(a.keys() - b.keys())
print(a.items() & b.items())  # { ('y', 2) }

# 现有字典构造一个排除几个指定键的新字典
c = {key: a[key] for key in a.keys() - {'z', 'w'}}
