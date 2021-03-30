"""
1. 定义父类：武器，数据：攻击力，行为：购买，攻击
    定义子类：枪，数据：射速，行为：攻击
    定义子类：手雷，数据：爆炸范围，行为：攻击
    创建相应对象，调用相应方法
"""


class Weapon:
    def __init__(self, atk_force):
        self.atk_force = atk_force

    def attack(self):
        raise NotImplementedError()


class Gun(Weapon):

    def __init__(self, atk_force, atk_speed):
        super().__init__(atk_force)
        self.atk_speed = atk_speed

    def attack(self):
        print("Gun is attacking!")


class Shoulei(Weapon):

    def __init__(self, atk_force, atk_range):
        super().__init__(atk_force)
        self.atk_range = atk_range

    def attack(self):
        print("Shoulei is attacking!")


g1 = Gun(100, 25)
s1 = Shoulei(200, 28)
g1.attack()
s1.attack()