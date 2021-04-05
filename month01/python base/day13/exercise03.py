# 练习3：定义函数，输入年月日，返回星期
import time

def date_to_week(year, month, day):
    week_dic = {
        6: "Sunday",
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday"
    }
    return week_dic[time.strptime("%d %d %d" % (year,month,day), "%Y %m %d")[6]]



print(date_to_week(2021,4,5))

