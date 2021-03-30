"""
    需求：老张开车去东北
    分而治之 -- 分解
    变化点：
"""

class Person:
    def __init__(self, name):
        self.name = name

    def go_to(self, type, str_pos):
        type.run(str_pos)

class Car:
    def run(self, str_pos):
        print("行驶到", str_pos)

p01 = Person("laozhang")
c01 = Car()
p01.go_to(c01, "dongbei")

# 练习1；小明在招商银行取钱。