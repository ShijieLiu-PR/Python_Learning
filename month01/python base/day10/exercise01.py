# 练习1；小明 在 招商银行 取钱。

class Person:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def withdraw(self, bank, count):
        print(self.name, bank.name, count)

class Bank:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def draw_money(self, person, value):
        if self.money >= value:
            self.money -= value
            person.money += value
            print(person.name, "取钱%d成功!" % (value))
        else:
            print("取钱失败！")

p01 = Person("小明", 0)
b01 = Bank("招商银行", 10000)
b01.draw_money(p01, 1000)