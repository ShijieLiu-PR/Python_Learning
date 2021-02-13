# 练习1：在控制台中获取一个整数，判断是奇数还是偶数，要求使用条件表达式
number = "even" if int(input("Please input an int:")) % 2 == 0 else "odd"
print(number)
