# 练习3：有若干个图形（圆形，矩形...），每种图形都可以计算面积。定义图形管理器，记录所有图形，提供计算总面积的方法。
# 要求：增加新的图形，不改变图形管理器的代码。
import math


class ShapeManager:
    def __init__(self):
        self.shape_list = list()

    def add_shape(self, shape):
        self.shape_list.append(shape)

    def total_area(self):
        sum = 0
        for item in self.shape_list:
            sum += item.area()
        return sum


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass


class Circle(Shape):
    def __init__(self, name, radius):
        super(Circle, self).__init__(name)
        self.radius = radius

    def area(self):
        return 3.14 * math.pow(self.radius, 2)


class Rectangle(Shape):
    def __init__(self, name, l, w):
        super(Rectangle, self).__init__(name)
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

sm = ShapeManager()
sm.add_shape(Circle("circle",1 ))
sm.add_shape(Rectangle("Rectangle",1, 1))
print(sm.total_area())