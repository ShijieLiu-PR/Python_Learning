# 4.回文（例如：上海自来水来自海上，奶牛产牛奶），判断输入的字符串是否是回文。提示：字符串反转
str_input = input("Please input your string:")
if str_input == str_input[::-1]:
    print("Yes")
else:
    print("No")