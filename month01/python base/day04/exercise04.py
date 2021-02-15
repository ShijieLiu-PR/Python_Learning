# 练习4：在控制中获取字符串，
str_input = input("Please input a string:")
#   1.打印第一个字符
print(str_input[0])
print(str_input[-len(str_input)])

#   2.打印最后一个字符
print(str_input[-1])
print(str_input[len(str_input)-1])

#   3.如果是奇数，打印中间字符
if len(str_input) % 2 != 0:
    print(str_input[len(str_input)//2])

#   4.打印倒数3个字符
print("4.打印倒数3个字符")
print(str_input[len(str_input)-3:len(str_input):])
print(str_input[len(str_input)-3::])
print(str_input[-3:])
print(str_input[-3::])
#   5.倒叙打印字符
print(str_input[::-1])
