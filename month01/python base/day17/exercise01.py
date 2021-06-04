
class Enemy:
    def __init__(self, id, name, atk, hp, atk_speed):
        self.id = id
        self.name = name
        self.atk = atk
        self.hp = hp
        self.atk_speed = atk_speed


list_enemy = [
    Enemy(101, "zhangsan", 100, 56, 3),
    Enemy(102, "lisi", 67, 0, 1),
    Enemy(103, "wangwu", 56, 7, 4),
    Enemy(104, "zhaoliu1112121", 120, 26, 2)
]
# 练习：
# 1.查找血量在10-50之间的敌人 filter
hp_select = filter(lambda e: 10 < e.hp < 50, list_enemy)
for item in hp_select:
    print(item.name, item.hp)

# 2.查找所有敌人的攻击力 map
atk_list = list(map(lambda e: e.atk, list_enemy))
print(atk_list)

# 3.根据攻击力对敌人列表进行降序排列

atk_descend = sorted(list_enemy, key=lambda e: e.atk, reverse=True)
for item in atk_descend:
    print(item.name, item.atk)

# 4。查找姓名字数最长的敌人
max_name = max(list_enemy, key=lambda e: len(e.name))
print(max_name.name)


