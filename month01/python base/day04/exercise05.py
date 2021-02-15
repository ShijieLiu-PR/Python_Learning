# 练习5：在控制台中输入一个整数，根据整数打印一个正方形。如下：
"""
    ****
    *  *
    *  *
    ****
"""
size = int(input("Please input an int:"))
for item in range(size):
    if item == 0 or item == size - 1:
        print("*" * size)
    else:
        print("*" + " " * (size - 2) + "*")
