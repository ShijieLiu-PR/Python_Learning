"""
    练习：
"""
class Enemy:
    """
    enemy class
    """
    def __init__(self, name = "", hp = 0, atk = 0, atk_speed = 0):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.atk_speed = atk_speed

    def print_self(self):
        print(self.name, self.hp, self.atk, self.atk_speed)

# 1.在控制台中输入3个敌人，存入列表
# 2.将敌人列表输出到控制台中


list01 = list()
e1 = Enemy("zhangsan", 3000, 120, 10)
e1.print_self()
for i in range(3):
    name = input("请输入第%d个敌人姓名：" % (i))
    hp = input("请输入第%d个敌人血量：" % (i))
    atk = input("请输入第%d个敌人攻击力：" % (i))
    atk_speed = input("请输入第%d个敌人攻击速度：" % (i))
    list01.append(Enemy(name, hp, atk, atk_speed))

for item in list01:
    print(item.name)
# 练习3:定义函数，在敌人列表中，根据姓名查找敌人对象。


def find_enemy(list_enemy, name):
    for item in list_enemy:
        if name == item.name:
            return item