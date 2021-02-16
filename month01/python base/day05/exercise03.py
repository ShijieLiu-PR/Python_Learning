# 练习3：在控制台中输入月和日，计算这是一年的第一天。
year = int(input("请输入年："))
month = int(input("请输入月："))
day = int(input("请输入日："))
Nth_day = 0
leap_year = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
day_of_month = (31,28,31,30,31,30,31,31,30,31,30,31)
# for i in range(month-1):
#     Nth_day += day_of_month[i]
Nth_day = sum(day_of_month[:month-1:])
Nth_day += day + 1 if leap_year and month > 2 else day
print("%d-%d-%d是这年的第%d天。"%(year,month,day,Nth_day))