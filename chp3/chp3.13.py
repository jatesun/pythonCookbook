"""
通用方法来计算一周中某一天上一次出现的日期，例如上一个周五的日期。
"""
"""
Topic: 最后的周五
Desc :
"""
from datetime import datetime, timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']


def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date


print(get_previous_byday('Monday'))
print(get_previous_byday('Tuesday'))  # Previous week, not today
print(get_previous_byday('Wednesday'))
print(get_previous_byday('Sunday', datetime(2012, 12, 21)))
print("==================")
# 大量的日期计算的话，你最好安装第三方包 python-dateutil 来代替使用 dateutil 模块中的 relativedelta() 函数执行同样的计算
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *

d = datetime.now()
print(d)
print(d + relativedelta(weekday=FR))  # 下一个周五
print(d + relativedelta(weekday=FR(-1)))  # 上一个周五
