# 1.练习：创建学生类，具有姓名，年龄等数据，具有学习、工作等方法。
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        print(self.name + "study!")

    def work(self):
        print(self.name + "work!")


s1 = Student("wukong", 28)
s2 = Student("bajie", 29)
s1.study()
s2.study()
s2 = s1
s1.name = "sunwukong"
print(s2.name)
