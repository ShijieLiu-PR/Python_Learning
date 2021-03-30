"""
    # 练习1：定义父类 -- 宠物， 行为：吃
    #       定义子类 -- 狗， 行为：防守xx
    #       定义子类 -- 鸟， 行为：飞
    #       创建相应的对象，调用相应的方法，使用isinstance和issubclass测试
"""

class Pet:
    def __init__(self, name):
        self.name = name

    def eat(self):
        pass


class Dog(Pet):
    def __init__(self, name, job):
        super(Dog, self).__init__(name)
        self.job = job

    def defend(self):
        pass


class Bird(Pet):
    def __init__(self, name):
        super(Bird, self).__init__(name)
    def fly(self):
        pass


p01 = Pet("Pet")
d01 = Dog("Dog")
b01 = Bird("Bird")

print(isinstance(b01, Pet))
print(isinstance(d01, Pet))