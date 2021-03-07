"""
2. 张三 教 李四 学习 python，李四 教 张三 玩游戏，张三 工作挣了 8000元， 李四工作挣了3000元。
    使用面向对象的思想描述以上场景。提示：对象与对象数据不同，类与类行为不同。

"""


class Person:
    def __init__(self, name, money, skill):
        self.name = name
        self.money = money
        self.skill = skill

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        self.__money = value

    @property
    def skill(self):
        return self.__skill

    @skill.setter
    def skill(self, value):
        self.__skill = value

    def teach(self, stu, skill):
        print(self.name + " teach " + stu.name + " " + skill)

    def work(self, money):
        self.money += money


p1 = Person("zs", 0, list())
p2 = Person("ls", 0, list())
p1.work(8000)
p2.work(3000)
p1.teach(p2, "play game")
p2.teach(p1, "study")
