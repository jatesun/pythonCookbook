"""
字符串格式的输入，但是你想将它们转换为 datetime 对象
datetime
"""
from datetime import datetime

text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
diff = z - y
print(diff)
