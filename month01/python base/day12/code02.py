"""
    内置可重写函数
"""

class Wife:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        #返回给人看
        return "我叫%s，今年%d岁！" % (self.name, self.age)

    def __repr__(self):
        #返回给解释器看
        return 'Wife("%s",%d)' % (self.name, self.age)

w01 = Wife("zs", 25)
print(w01)
w02 = eval(w01.__repr__())
w01.name = "lisi"
print(w02.name)
