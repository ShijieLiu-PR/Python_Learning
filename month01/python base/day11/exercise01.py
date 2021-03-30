"""
1.使用面向对象的思想，写出如下场景：
    玩家（攻击力）攻击敌人，敌人受伤（血量）后掉血，还可能死亡（播放动画）。
    敌人（攻击力）攻击力攻击玩家，玩家（血量）受伤后碎屏，还可能死亡（游戏结束）
"""


class Player:
    """
        玩家类
    """
    def __init__(self, atk, hp):
        self.atk = atk
        self.hp = hp

    def attack(self, enemy):
        print("Player is attacking you!")
        enemy.damage(self.atk)

    def damage(self, value):
        self.hp -= value
        if self.hp <= 0:
            self.__death()
            return 0
        print("Player is attacked!")

    def __death(self):
        print("Player is dead, game over!")


class Enemy:
    def __init__(self, hp, atk):
        self.hp = hp

    def damage(self, value):
        self.hp -= value
        if self.hp <= 0:
            self.__death()
            return
        print("Enemy is attacked!")

    def attack(self, player):
        player.damage(self.atk)

    def __death(self):
        print("Enemy is dead, play animation!")

p01 = Player(100,50)
e01 = Enemy(60, 10)
p01.attack(e01)