"""
你需要使用路径名来获取文件名，目录名，绝对路径等等。
"""
import os

path = '/Users/beazley/Data/data.csv'
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.join('tmp', 'data', os.path.basename(path)))

path = '~/Data/data.csv'
print(os.path.expanduser(path))

# 测试文件是否存在
print(os.path.exists('etc/passwd'))
# 获取文件夹文件列表
names = os.listdir('~/Data')
