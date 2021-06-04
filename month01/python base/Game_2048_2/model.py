"""
    数据模型模块
"""
import random


class Location:
    """
        位置类
    """
    def __init__(self, r, c):
        self.r_index = r
        self.c_index = c

    @property
    def r_index(self):
        return self.__r_index

    @r_index.setter
    def r_index(self, value):
        self.__r_index = value


class Direction:
    """
        方向
    """
    up = 0
    down = 1
    left = 2
    right = 3


if __name__ == "__main__":
    x =2
    var = 4 if x >9 else 5
    print(var)
    list01 = [(1,2),(3,4),(5,6),(7,8),(9,10)]
    loc = random.choices(list01,[1,1,1,1,6])
    print(loc)