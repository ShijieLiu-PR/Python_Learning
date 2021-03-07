"""
    封装
"""


# 注意：只是通过两个方法读写私有变量
class Wife02:
    def __init__(self, name, age):
        self.set_name(name)
        # 缺点；缺乏对数据的封装，外界可以所以赋值。
        # 私有成员：障眼法（解释器会改变双下划线开头的变量名）
        # self.__age = age
        self.set_age(age)

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if 20 <= value <= 30:
            self.__age = value
        else:
            print("i dont want")


w01 = Wife02("lili", 28)

# 创建的新属性
w01.age = 50
print(w01.__dict__)

# 找不到双下划线的开头的数据。
# print(w01.__age)
# 通过下划线加类名可以找到双下划线开头的数据。

w02 = Wife02("fangfang", 39)
w02.set_age(38)
