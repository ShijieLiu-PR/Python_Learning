"""
    选择语句
"""
# sex = input("Please input gender:")
# if sex == "male":
#     print("hello man")
# elif sex == "female":
#     print("hello woman")
# else:
#     print("unknown sex")

#练习7：在控制台中输入一个整数，如果是奇数显示奇数，如果是偶数显示偶数。
num01 = int(input("Please input a number:"))
if num01%2 == 0:
    print("Even")
else:
    print("Odd")


#练习8：在控制台中输入一个年份，如果是闰年，则显示闰年，否则显示平年。

year = int(input("Please input year:"))
result = year % 4 == 0 and year % 400 != 0 or year % 400 == 0
if result:
    print("闰年")
else:
    print("平年")