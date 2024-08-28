"""
你想为 sort() 操作创建一个很短的回调函数，但又不想用 def 去写一个单行函数， 而是希望通过某个快捷方式以内联方式来创建这个函数。
"""
add = lambda x, y: x + y
print(add(2, 3))


def add(x, y):
    return x + y
