"""
    多继承
"""

class A:
    def m(self):
        print("a -- m")

class B(A):
    def m(self):
        print("b -- m")


class C(A):
    def m(self):
        print("c -- m")

class D(C,B):
    def m(self):
        super().m()
        print("d -- m")

#调用父级同名方法，执行顺序（继承列表顺序。）
d01 = D()
d01.m()
print(D.mro())
