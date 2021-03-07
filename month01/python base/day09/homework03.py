"""
3. 创建技能类（技能名称，冷却时间，持续时间，攻击距离）
    要求：使用属性封装变量。
    创建技能列表：
    a.查找名称是“降龙十八掌”的技能对象
    b.查找持续时间大于10s的所有技能对象
    c.查找攻击距离最远的技能对象
    d.按照持续时间对列表升序排列
"""


class Skill:
    def __init__(self, name, cd, time, atk_dis):
        self.name = name
        self.cd = cd
        self.time = time
        self.atk_dis = atk_dis

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def cd(self):
        return self.__cd

    @cd.setter
    def cd(self, value):
        self.__cd = value

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, value):
        self.__time = value

    @property
    def atk_dis(self):
        return self.__atk_dis

    @atk_dis.setter
    def atk_dis(self, value):
        self.__atk_dis = value


def find_skill_by_name(list_target, name):
    for item in list_target:
        if item.name == name:
            return item
    return None


def find_skill_by_time(list_target, time):
    list01 = list()
    for item in list_target:
        if item.time > time:
            list01.append(item)
    return list01


def find_skill_max_distance(list_target):
    target_skill = list_target[0]
    for item in list_target:
        if item.time > target_skill.time:
            target_skill = item
    return target_skill


def sort_skill_by_cd(list_target):
    for i in range(len(list_target)):
        for j in range(i + 1, len(list_target)):
            if list_target[i].cd > list_target[j].cd:
                list_target[i], list_target[j] = list_target[j], list_target[i]



skill_list = [
    Skill("降龙十八掌", 10, 1, 86),
    Skill("凌波微步", 12, 10, 45),
    Skill("九阳神功", 5, 3, 120),
    Skill("化骨绵掌", 7, 8, 56),
]

s01 = find_skill_by_name(skill_list,"降龙十八掌")
print(s01.__dict__)
list01 = find_skill_by_time(skill_list,5)
for item in list01:
    print(item.__dict__)
s02 = find_skill_max_distance(skill_list)
print(s02.__dict__)
sort_skill_by_cd(skill_list)
for item in skill_list:
    print(item.name, item.cd)