"""
    1.创建技能类（编号，技能名称，冷却时间，攻击力，魔法消耗）
    创建技能列表：
        -- 定义函数：查找编号是101的技能对象
        -- 定义函数：查找冷却时间为0的所有技能对象
        -- 定义函数：查找攻击力大于5的所有技能对象
        -- 定义函数：查找攻击力大于10，并且不需要消耗乏力的所有技能。
"""


class Skill:
    def __init__(self, id, name, cd, atk, magic):
        self.id = id
        self.name = name
        self.cd = cd
        self.atk = atk
        self.magic = magic

    def __str__(self):
        return "id:%d, name:%s, cd:%d, atk:%d, magic:%d" % (self.id, self.name, self.cd, self.atk, self.magic)


list01 = [
    Skill(101, "降龙十八掌", 2, 130, 15),
    Skill(102, "六脉神剑", 0, 100, 35),
    Skill(103, "一阳指", 2, 190, 0),
    Skill(104, "葵花点穴手", 0, 120, 15),
    Skill(105, "韦陀掌", 5, 90,0),
]


def find_id(target):
    for item in target:
        if item.id == 101:
            return item


#
#
# def find_cd(target):
#     for item in target:
#         if item.cd == 0:
#             yield item
# print("--------------------------------------------------------------")
#
# result = find_cd(list01)
# for item in result:
#     print(item)
#
#
# def find_atk(target):
#     for item in target:
#         if item.atk > 5:
#             yield item
#
# print("--------------------------------------------------------------")
# iterator = find_atk(list01)
# print(iterator)
# for item in iterator:
#     print(item)
#
# # 通过生成器创建列表
# # 由惰性查找（优势：节省内存） 转换为 立即查找（灵活获取结果）


def find_atk_magic(target):
    for item in target:
        if item.atk > 5 and item.magic == 0:
            yield item



for item in find_atk_magic(list01):
    print(item)