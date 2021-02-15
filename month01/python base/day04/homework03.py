# 3.在控制台中循环录入字符串，输入q时退出，然后显示一个新的字符串。
list01 = []
while True:
    str_input = input("Please input string:")
    if str_input == "q":
        break
    else:
        list01.append(str_input)
print("".join(list01))
