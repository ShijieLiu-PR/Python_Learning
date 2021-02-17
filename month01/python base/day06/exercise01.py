# 练习1：在控制台中随意录入多个字符串，按q退出，再显示所有不重复的字符串
s01 = set()
while True:
    chr_input = input("请输入一个字符串:")
    if chr_input == "q":
        break
    else:
        s01.add(chr_input)
print(s01)