# 练习5：定义敌人类（姓名，攻击力，攻击速度（0-10），血量（0-100））
# 练习6：修改练习5的Enemy类，使用属性封装变量。

class Enemy:
    def __init__(self, name="", atk=10, atk_speed=1, hp=50):
        self.__name = name
        self.atk = atk
        self.atk_speed = atk_speed
        self.hp = hp

    @property
    def name(self):
        return self.__name

    # @name.setter
    # def name(self, value):
    #     self.__name = value

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        self.__atk = value

    @property
    def atk_speed(self):
        return self.__atk_speed

    @atk_speed.setter
    def atk_speed(self, value):
        self.__atk_speed = value

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp = value

    def print_enemy(self):
        print("Enemy name is %s, hp is %d, atk is %d, atk_speed is %d" % (self.name, self.hp, self.atk, self.atk_speed))

e01 = Enemy("zs", 29, 4, 68)
e01.print_enemy()
print(e01.name)
print(e01.name)
print(e01.__dict__)