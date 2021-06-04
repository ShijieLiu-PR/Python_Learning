# 练习：
# 解决的问题：筛选对象
# 技能列表 -- 转换为编号列表
# 技能列表 -- 转换为名称列表
from common.custom_list_tools import ListHelper

class Skill:
    def __init__(self, id, name, cd, atk, magic):
        self.id = id
        self.name = name
        self.cd = cd
        self.atk = atk
        self.magic = magic


list_skills = [
    Skill(101, "降龙十八掌", 2, 130, 15),
    Skill(102, "六脉神剑", 0, 100, 35),
    Skill(103, "一阳指", 2, 190, 0),
    Skill(104, "葵花点穴手", 0, 120, 15),
    Skill(105, "韦陀掌", 5, 90,0),
]

from common.custom_list_tools import ListHelper

list01 = list(ListHelper.select(list_skills, lambda item: item.id))
print(list01)

list02 = list(ListHelper.select(list_skills, lambda item: item.name))
print(list02)

list03 = list(ListHelper.select(list_skills, lambda item: (item.id, item.name)))
print(list03)