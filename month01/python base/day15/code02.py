"""
    迭代器
"""


class Skill:
    pass


class SkillIterator:
    def __init__(self, target):
        self.target = target
        self.index = 0

    def __next__(self):
        if self.index >= len(self.target):
            raise StopIteration("out of range")
        else:
            res = self.target[self.index]
            self.index += 1
            return res


class SkillManager:
    def __init__(self, skills):
        self.skills = skills

    def __iter__(self):
        # 创建迭代器对象
        return SkillIterator(self.skills)


manager = SkillManager([Skill(), Skill(), Skill()])

for item in manager:
    print(item)


# iterator = manager.__iter__()
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     except Exception as e:
#         print(e.args)
#         break

