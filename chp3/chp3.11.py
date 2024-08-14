"""
你想从一个序列中随机抽取若干元素，或者想生成几个随机数。
random模块
"""
import random

values = [1, 2, 3, 4, 5, 6]
print(random.choice(values))
print(random.sample(values, 2))
random.shuffle(values)
print(values)
print(random.randint(0, 10))  # 随机生成数字
random.random()# 0-1浮点数

