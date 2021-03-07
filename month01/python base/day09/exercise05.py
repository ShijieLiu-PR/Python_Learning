# 练习5：定义敌人类（姓名，攻击力，攻击速度（0-10），血量（0-100））
class Enemy:
    def __init__(self, name, hp, atk, atk_speed):
        pass
        self.set_name(name)
        self.set_hp(hp)
        self.set_atk(atk)
        self.set_atk_speed(atk_speed)

    def set_name(self, value):
        self.__name = value

    def get_name(self):
        return self.__name

    def set_hp(self, value):
        if 0 <= value <= 100:
            self.__hp = value
        else:
            self.__hp = 0
            print("hp is out of range!")

    def get_hp(self):
        return self.__hp

    def set_atk(self, value):
        self.__atk = value

    def get_atk(self):
        return self.__atk

    def set_atk_speed(self, value):
        if 0 <= value <= 10:
            self.__atk_speed = value
        else:
            self.__atk_speed = 0
            print("atk_speed is out of range!")


e01 = Enemy("zs", 100, 200, 1)
print(e01.__dict__)
print(e01._Enemy__atk)
