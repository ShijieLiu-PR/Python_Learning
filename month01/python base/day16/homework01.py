"""
    目标1：熟练应用ListHelper
    --创建敌人类（编号/姓名/攻击力/血量/攻击速度）
    --创建敌人列表
练习：

"""
from day16.common.custom_list_tools import ListHelper

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

# # 1.查找所有血量为0的人
# list01 = list(ListHelper.find_all(list_enemy, lambda item: item.hp == 0))
# print(list01)
# # 2.查找所有血量大于0的人
# list02 = list(ListHelper.find_all(list_enemy, lambda item: item.hp > 0))
# # 3.计算所有攻击力的总和
# atk_sum = ListHelper.sum(list_enemy, lambda item:item.atk)
# print(atk_sum)
# # 4.查找编号是101的敌人
# p101 = list(ListHelper.find_all(list_enemy, lambda item: item.id == 102))
# print(p101[0].name)
# # 5.查找攻击速度在5到10之间的敌人
# atk_sel = list(ListHelper.find_all(list_enemy, lambda item: 2 < item.atk_speed < 5))
# for item in atk_sel:
#     print(item.name)
# # 6.查找所有敌人的姓名
# name_list = list(ListHelper.select(list_enemy, lambda item:item.name))
# print(name_list)

"""
    解决的问题：获取满足条件的最后一个对象。
    获取最后1个血量大于0的敌人
    获取攻击速度大于5的最后一个敌人
"""
#
# enemy_last_alive = ListHelper.last_match(list_enemy, lambda item:item.hp > 0)
# print(enemy_last_alive.name)
# enemy_last_atk = ListHelper.last_match(list_enemy, lambda item:item.atk_speed > 3)
# print(enemy_last_atk.name)
#
"""
    解决的问题：获取满条件的对象总数
    获取生命值大于0的敌人总数
    获取攻击速度小于20的敌人总数
"""
# sum_alive = ListHelper.sum(list_enemy, lambda item: item.hp > 0)
# sum_atk_speed = ListHelper.sum(list_enemy, lambda item: item.atk_speed > 3)
# print(sum_alive)
# print(sum_atk_speed)


"""
    解决的问题：判断列表中是否包含某个元素
    判断列表中是否存在生命值为0的敌人
    判断列表中是否存在攻击速度小于20的敌人
"""
# hp_equal_0 = ListHelper.exist(list_enemy, lambda item:item.hp == 0)
# atk_speed_greater_x = ListHelper.exist(list_enemy, lambda item:item.atk_speed > 3)
# print(hp_equal_0)
# print(atk_speed_greater_x)



"""
    删除hp等于0的敌人
    删除编号是101的敌人
    删除攻击力小于5的敌人
"""

list02 = [5, 7, 9, 4, 2, 3, 5, 6]
ListHelper.delete(list02, lambda item: item == 5)
print(list02)