"""
    字符串字面值
"""
str01 = "大家好"
str01 = '大家好'
# 以上单双引号没有区别
str01 = '''大家好'''
str01 = """大家好"""
# 三引号：可见即所得
str01 = """大家好"""
str02 = '我爱"Python"'
print(str02)

# 转义符：
str03 = "我爱\"Python\""
print(str03)

str04 = "大家好，\n我是liusj"
print(str04)
a = r"c:\a\b.txt"
print(a)

# 格式化字符串
name = "qtx"
age = 32
score = 96.5124345
msg = "我的名字是：xx，年龄是：xx"
print("我的名字是：%s，年龄是：%s，我的成绩是：%-06.2f" % (name, age, score))

str05 = "整数是：%05.3d"%(32.123456)
print(str05)
str06 = "整数是：%0-5.3d"%(32.123456)
print(str06)

num01 = 1.234567
num01 = round(num01, 4)
print(num01)