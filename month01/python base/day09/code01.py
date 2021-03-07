"""
    实例成员
"""


class Wife:
    pass
    def print_self(self):
        print("hello world")


w01 = Wife()
# 语法上支持，但是在实际项目中不建议这么做。
# 创建实例成员可以不在类中，实际项目中，仍然会在__init__函数中。
w01.name = "Lily"
print(w01.name)
print(w01.__dict__)
w01.age = 21
print(w01.__dict__)
w01.print_self()
Wife.print_self(w01)

