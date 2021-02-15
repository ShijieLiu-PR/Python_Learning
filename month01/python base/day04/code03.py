"""
    字符串操作
"""
# 1.数学运算
str01 = "wukong"
str02 = "bajie"
#创建新对象
str03 = str01 + str02
print(str03)
#容器可以与数字相乘
str04 = str01 * 3
print(str04)

print(str01 > str02)
for item in str01:
    print(ord(item))

# 2.成员运算
str03 = "猥琐发育，别浪！"
print("猥琐" in str03)

# 3.索引
str04 = "abcdef"
print(str04[0])
print(str04[len(str04) - 1])
print(str04[-1])

# 4.切片slice
str05 = str04[0:3:2]
print(str05)
print(str04[::])
print(str04[::-1])
print(str04[1:19]) #切片即使越界，也不会报错
print("----------------")
print(str04[3:1:-1])