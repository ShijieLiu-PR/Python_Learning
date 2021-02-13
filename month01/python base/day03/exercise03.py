# 练习3：在控制台中分别输入两个整数，一个作为开始值，一个作为结束值，请输入中间数字。
min = int(input("Please input min:"))
max = int(input("Please input max:"))
while True:
    min += 1
    if min < max:
        print(min)
    else:
        break
