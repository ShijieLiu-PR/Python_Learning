"""
    作业1：
解决的问题1：
    获取敌人列表中攻击力最小的敌人，使用内置高阶函数和ListHelper两种方法实现
解决的问题2：
    根据血量对敌人列表进行降序排列，使用内置高阶函数和ListHelper两种方法实现

    在ListHelper中，定义万能排序（任意条件/升序/降序）方法。
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

import sys
sys.path.append("C:\\Users\\Liusj\\Desktop\\Python_Learning\\month01\\python base")
from day16.common.custom_list_tools import ListHelper
# atk_min = min(list_enemy, key=lambda e: e.atk)
# print(atk_min.name, atk_min.atk)
# atk_min2 = ListHelper.min(list_enemy, lambda e: e.atk < list_enemy[0].atk)
# print(atk_min2.name, atk_min2.atk)
#
# ascend = ListHelper.ascend(list_enemy, lambda e: e.atk)
# for item in ascend:
#     print(item.atk, item.name)
#
# descend = ListHelper.descend(list_enemy, lambda e:e.atk)
# for item in ascend:
#     print(item.atk, item.name)

# min_atk = ListHelper.get_min(list_enemy, lambda e: e.atk)
# print(min_atk.name, min_atk.atk)
# max_atk = ListHelper.get_max(list_enemy, lambda e: e.atk)
# print(max_atk.name, max_atk.atk)

# ascend_atk = sorted(list_enemy, key=lambda e: e.atk, reverse=False)
# for item in ascend_atk:
#     print(item.name, item.atk)
#
# descend_atk = sorted(list_enemy, key=lambda e: e.atk, reverse=True)
# for item in descend_atk:
#     print(item.name, item.atk)
#
# ascend_atk = ListHelper.sort(list_enemy, lambda a, b: a.atk > b.atk)
# for item in ascend_atk:
#     print(item.name, item.atk)
#

descend_atk = ListHelper.sort(list_enemy, lambda a, b: a.atk < b.atk)
for item in descend_atk:
    print(item.name, item.atk)
