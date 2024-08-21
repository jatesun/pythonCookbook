"""
遍历一个可迭代对象中的所有元素，但是却不想使用for循环

"""
with open("etc/passwd") as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line)

# 需要对迭代精确控制
items = [1, 2, 3]
it = iter(items)
print(next(it))
