# 练习1：创建老婆类，随意实例化对象，统计老婆对象数量(定义方法)。


class Wife:
    count = 0

    @classmethod
    def get_count(cls):
        return cls.count

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Wife.count += 1

    def print_self(self):
        print(self.name + "的年龄是：" + str(self.age) + ".")

list01 = list()
for i in range(5):
    list01.append(Wife("wife" + str(i),i + 1))

for item in list01:
    item.print_self()

# print(Wife.get_count())
list01[0].get_count()