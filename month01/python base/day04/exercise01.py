# 练习1：在控制台中获取一个字符串，打印每个字符的编码值。
str_input = input("Please input string:")
for item in str_input:
    print(ord(item))
else:
    print("Complete!")

print(ord("a"))
print(bin(11))