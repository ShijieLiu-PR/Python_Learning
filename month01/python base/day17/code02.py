"""
    高阶函数
"""

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
    Enemy(103, "wangwu", 56, 0, 4),
    Enemy(104, "zhaoliu", 120, 26, 2)
]

# 过滤出编号大于102的敌人
for item in filter(lambda e: e.id > 102, list_enemy):
    print(item.id, item.name)

# map
# 映射出所有敌人的编号
list_id = list(map(lambda e: e.id, list_enemy))
print(list_id)

# sorted
res = list(sorted(list_enemy, key = lambda e: e.hp))
for item in res:
    print(item.name, item.hp)

# max
list01 = [4,5,6]
list02 = [8,5,9]
res = max(list_enemy, key = lambda e: e.atk)
print(res.atk, res.name)
res = max(list02,key = lambda e:e)
print(res)