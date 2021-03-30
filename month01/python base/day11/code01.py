"""
    继承语法
"""
# 学生  与  老师  在某种概念上是统一的


class Person:
    def __init__(self, name):
        self.name = name

    def say(self):
        print("speak-p")


class Student(Person):

    def __init__(self, name, score):
        super().__init__(name)
        self.score = score

    def study(self):
        print("study")


class Teacher(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def teach(self):
        print("teach")


p01 = Person("zhangsan")
p01.say()

s01 = Student("lisi",68)
s01.say()

t01 = Teacher("wanger", 100000)
t01.say()


print(issubclass(Student, Person))
print(issubclass(Student, Teacher))