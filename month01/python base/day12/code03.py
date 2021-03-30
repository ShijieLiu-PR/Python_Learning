"""
    运算符重载
"""
print("a" + "b")


class Vector:
    """
        向量类
    """
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        # self.x += other
        # return self
        return Vector(self.x + other)

    def __str__(self):
        return "Vector(%d)" % self.x

v01 = Vector(10)
v02 = v01 + 5
print(id(v01))
print(id(v02))

print(v01)
print(v02)
