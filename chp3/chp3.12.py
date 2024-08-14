"""
你需要执行简单的时间转换，比如天到秒，小时到分钟等的转换。
为了执行不同时间单位的转换和计算，请使用 datetime 模块
"""
from datetime import timedelta, datetime

a = timedelta(days=2, hours=6)  # 时间段
b = timedelta(hours=4.5)
c = a + b
print(c.days)
print(c.seconds)
print(c.total_seconds())
a = datetime(2012, 9, 23)
print(a + timedelta(days=10))
b = datetime(2012, 12, 21)
d = b - a
print(d.days)
now = datetime.now()
print(now)
print(now + timedelta(minutes=10))
# datetime 会自动处理闰年
# 处理时区，模糊时间范围，节假日计算等等， 可以考虑使用 dateutil模块

