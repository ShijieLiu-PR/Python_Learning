# 练习2：在控制台中获取一个年份，如果是闰年给变量day赋值29，否则赋值28
year = int(input("Please input year:"))
day = 29 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else 28
print(day)