#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 通过导入 __future__ 包来兼容 Python3.x print
# 如果使用了 Python3.x 可以删除此行引入
from __future__ import print_function

from datetime import datetime


now = datetime.now() # current date and time

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time = now.strftime("%Y-%m-%dT%H:%M:%S.%NZ")
print("date and time:",date_time)