""""""
"""
练习1：在控制台中获取月份，打印季节（春夏秋冬）
"""

#month = int(input("Please input month:"))
# --method 1
# if month >= 1 and month <= 3:
#     print("spring")
# elif month >= 4 and month <= 6:
#     print("summer")
# elif month >= 7 and month <= 9:
#     print("autumn")
# elif month >= 10 and month <= 12:
#     print("winter")
# else:
#     print("error month input!")

# --method 2
# if month >= 1:
#     if month <= 3:
#         print("spring")
#     elif month <= 6:
#         print("summer")
#     elif month <= 9:
#         print("autumn")
#     elif month <= 12:
#         print("winter")
#     else:
#         print("error month input!")
# else:
#     print("error month input")

"""
    练习2：在控制台中输入季度，显示该季度中的月份。
"""
# quarter = int(input("Please input quarter(1,2,3,4):"))
# if quarter == 1:
#     print("1,2,3")
# elif quarter == 2:
#     print("4,5,6")
# elif quarter == 3:
#     print("7,8,9")
# elif quarter == 4:
#     print("10,11,12")
# else:
#     print("error quarter input!")

"""
    练习3：在控制台中输入一个月份，返回该月份的天数。
"""
# month = int(input("Please input month(1-12):"))
# if 1 <= month <= 12:
#     if month == 2:
#         print("28")
#     elif month == 4 or month == 6 or month == 9 or month == 11:
#         print("30")
#     else:
#         print("31")
# else:
#     print("error month input!")

"""
条件表达式
"""
# sex = None
# if input("") == "male":
#     sex = 0
# else:
#     sex = 1
# print(sex)

sex = 0 if input() == "male" else 1
print(sex)
# 练习1：在控制台中获取一个整数，判断是奇数还是偶数，要求使用条件表达式
# 练习2：在控制台中获取一个年份，如果是闰年给变量day赋值29，否则赋值28
