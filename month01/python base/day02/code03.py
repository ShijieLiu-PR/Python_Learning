"""
    逻辑运算符  与and 或or 非not
    身份运算符
"""
# print(True and False)
# print(True and True)
# print(False and False)
# print(False and True)

# 短路逻辑
# print(1 > 2 or input("Please input:") == "a")

#身份运算符
# num01 = 800
# num02 = 800
# num03 = 900
# print(num01 is num02)
# print(id(num01) == id(num02))
# print(num01 is num03)

#练习4：
#   闰年判断：
#   条件1：年份能被4整除，但不能被100整除
#   条件2：年份能被400整除
#   在控制台中获取年份
#   判断是否为闰年，如果是显示True，反之显示False
# year = int(input("Please input year:"))
# condition1 = year % 4 == 0 and year % 100 != 0
# condition2 = year % 400 == 0
# result = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
# print(result)

#练习5：在控制台中获取一个4位整数1234
#   计算每位相加和 1+2+3+4
# num01 = int(input("Please input a int:"))
# sum = 0
# sum += num01 % 10
# num01 //= 10
# sum += num01 % 10
# num01 //= 10
# sum += num01 % 10
# num01 //= 10
# sum += num01 % 10
# print("sum=", sum)

#练习6：在控制台中获取一个总秒数，计算几小时几分钟几秒钟。
seconds = int(input("Please input seconds:"))
minutes = seconds // 60
seconds %= 60
hours = minutes // 60
minutes %= 60
print("%s hours %s minutes %s seconds" % (hours,minutes,seconds))