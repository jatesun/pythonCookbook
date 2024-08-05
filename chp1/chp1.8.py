"""
怎样在数据字典中执行一些计算操作（比如求最小值、最大值、排序等等）？
通常需要使用 zip() 函数先将键和值反转过来
"""
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}
# for key in prices:
#     print(key, prices[key])

min_price = min(zip(prices.values(), prices.keys()))
print(min_price)
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)
#
# # 可以使用 zip() 和 sorted() 函数来排列字典数据：
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

# 需要注意的是 zip() 函数创建的是一个只能访问一次的迭代器
prices_and_names = zip(prices.values(), prices.keys())
for key in prices_and_names:
    print(key + prices_and_names[key])  # 只能访问key多次，value不可以。只能迭代一次。
print(min(prices_and_names))  # OK
print(max(prices_and_names))  # ValueError: max() arg is an empty sequence


