# 练习2：根据月份计算天数。
month = int(input("请输入月份："))
day_of_month = (31,28,31,30,31,30,31,31,30,31,30,31)
month1 = (2,)
month2 = (4,6,9,11)
month3 = (1,3,5,7,8,10,12)
if month in month1:
    print("28")
elif month in month2:
    print("30")
elif month in month3:
    print("31")
else:
    print("error month")

print(day_of_month[month-1])