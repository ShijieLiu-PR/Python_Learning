"""
3. 创建学生类，具有姓名、性别、年龄、成绩，具有方法：print_self
    --定义函数，在学生列表中，根据姓名查找学生对象。
    --定义函数，在学生列表中，根据性别查找所有学生对象。
    --定义函数，在学生列表中，查找年龄大于20，成绩大于60的所有学生对象。
"""


class Student:
    def __init__(self, name="", age=0, sex="", score=0):
        self.name = name
        self.age = age
        self.sex = sex
        self.score = score


list_student = [
    Student("zs", 18, "male", 87),
    Student("lisi", 19, "female", 56),
    Student("ww", 18, "male", 56)
]


def find_by_name(list_stu, name):
    for item in list_stu:
        if item.name == name:
            return item


def find_by_sex(list_stu, sex):
    list01 = []
    for item in list_stu:
        if item.sex == sex:
            list01.append(item)
    return list01


def find_by_age_score(list_stu, age, score):
    list01 = []
    for item in list_stu:
        if item.age <= age and item.score > score:
            list01.append(item)
    return list01


stu = find_by_name(list_student, "ww")
print(stu.age)