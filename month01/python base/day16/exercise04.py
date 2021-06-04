# 练习：
# 解决的问题：求和
# 技能列表 -- 所有技能编号的和
# 技能列表 -- 所有技能cd的和
import sys

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
sum_id = ListHelper.sum(list_skills, lambda item: item.id)
print(sum_id)

sum_cd = ListHelper.sum(list_skills, lambda item: item.cd)
print(sum_cd)


print(sys.path)
print(__name__)