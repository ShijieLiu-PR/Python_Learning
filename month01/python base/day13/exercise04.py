# 练习4：定义函数，根据生日，返回活了多少天
import time
def date_to_days(year, month, day):
    timestring = "%d %d %d" % (year, month, day)
    start_day = time.mktime(time.strptime(timestring, "%Y %m %d"))
    end_day = time.mktime(time.localtime())
    return (end_day - start_day)// (3600*24)



print(date_to_days(1984,10,23))