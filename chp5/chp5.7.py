"""
读写压缩文件
"""
import gzip

with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()

import bz2
with bz2.open('somefile.bz2', 'rt') as f:
    text = f.read()

