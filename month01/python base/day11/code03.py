"""
    继承  -- 设计思想
    面向对象设计原则
    1. 开闭原则
        对扩展开放，对修改关闭
    2. 依赖倒置（依赖抽象）
        使用抽象，而不是具体。
"""


class Person:
    def __init__(self, name):
        self.name = name

    def go_to(self, vehicle, pos):
        vehicle.Transport()


class Vehicle:
    def Transport(self, pos):
        raise NotImplementedError()


class Car(Vehicle):
    def Transport(self, pos):
        print("行驶到", pos)


class Airplane(Vehicle):
    def Transport2(self, pos):
        print("飞到", pos)


a01 = Airplane("beijing")
a01.Transport()