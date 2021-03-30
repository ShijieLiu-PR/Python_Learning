# 练习2：实现向量类于整数做减法和乘法运算
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

    def __mul__(self, other):
        return Vector(self.x * other)

    def __rmul__(self, other):
        return Vector(self.x * other)

    def __floordiv__(self, other):
        return Vector(self.x / other)

    def __str__(self):
        return "Vector(%d)" % self.x

v01 = Vector(10)
v02 = v01 * 5
v03 = v01 // 3

v04 = 5 * v01
print(v01)
print(v02)
print(v03)
print(v04)

list01 = [1,2,3]
print(id(list01))
list01 += [4]
print(id(list01))