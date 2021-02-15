# 练习2：在控制台中循环输入编码值，显示字符，直到输入负数时退出。
while True:
    int_input = int(input("Please input ord:"))
    if int_input < 0:
        break
    else:
        print(chr(int_input))

