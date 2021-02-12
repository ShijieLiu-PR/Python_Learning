"""
    数据类型
"""
# 1.整数 int
# 十进制
num01 = 100
# 二进制
num02 = 0b11
print(num02)
# -- 八进制
num03 = 0o10
print(num03)
# -- 十六进制
num04 = 0x1b
print(num04)
# 小数对象池
a = 100
b = 100

# id()返回变量存储的地址
print(id(a))
print(id(b))

# 2.浮点型 float
f01 = 1.0
f02 = 1.234e2
print(f02)
f02 = 1.234e-2
print(f02)

# 3.字符串string
s01 = "唐僧"
s02 = "10"
s03 = "1.5"
print(s02 + s03)
# 4.复数complex
c01 = 5+1j
print(c01)

# 5.布尔bool
b01 = True
b02 = False
b03 = 1 > 3
print(b03)

# 6.数据类型的转换
str_score = input("请输入成绩：")
# 从input函数的结果就是str，如果需要做数学运算，必须转换成数字。
str_score = float(str_score)
print(type(str_score))
b04 = bool("False")
print(b04)

#练习：在控制台中录入学生信息（姓名，年龄，性别，成绩）
#在一行输出：
#格式：我的姓名是：xxx，年龄是：xxx，性别是：xxx，成绩是：xxx
name = input("请输入姓名：")
age = int(input("请输入年龄："))
sex = input("请输入性别：")
score = float(input("请输入成绩："))
print("我的姓名是：%s,年龄是：%d，性别是：%s，成绩是：%f" % (name, age, sex, score))
print("我的姓名是：" + name + "，年龄是：" + str(age) + ",性别是：" + sex + "，成绩是：" + str(score))
