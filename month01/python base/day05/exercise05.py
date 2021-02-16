# 练习5：在控制台中录入一个字符串，打印这个字符串中的字符以及出现的次数。
str_input = input("请输入一个字符串:")
dict01 = {}
for item in str_input:
    if item not in dict01:
        dict01[item] = 1
    else:
        dict01[item] += 1
print(dict01)