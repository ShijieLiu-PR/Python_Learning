"""
    标准库 -- 时间
"""

from time import *
# time方法返回当前时间戳，即从1970年后经过的浮点秒数。

print(time())
# 时间元组
lt = localtime()
print(lt)
print(lt[3])

strtime = strftime("%Y-%m-%d %H:%M:%S", localtime())
print(strtime)
strptime("2019 04 08","%Y %m %d")
