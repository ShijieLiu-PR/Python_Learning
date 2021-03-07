"""
    00 01 02
    10 11 12
    20 21 22

    需求：在某个元素基础上，获取每个方向，指定数量的元素
    10 向右  2   -> 11 12
    21 向上  2   -> 11 01

"""


class Vector:
    """
        向量
    """

    # 实例方法
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # 将函数放到类中就是静态方法
    @staticmethod
    def right():
        return Vector(0, 1)

    @staticmethod
    def up():
        return Vector(-1, 0)

    @staticmethod
    def left():
        return Vector(0, -1)

    @staticmethod
    def down():
        return Vector(1, 0)

    @staticmethod
    def right_up():
        return Vector(-1, 1)


class DoubleListHelper:
    """
        二维列表助手类
        定义：在开发过程中，所有对二维列表的常用操作。
    """

    @staticmethod
    def get_elements(list_target, v_pos, v_dir, count):
        result = []
        # 位置 1 0  ->  方向 0 1
        for i in range(count):
            v_pos.x += v_dir.x
            v_pos.y += v_dir.y
            result.append(list_target[v_pos.x][v_pos.y])
        return result

# 测试...


list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"]
]

list02 = DoubleListHelper.get_elements(list01, Vector(1, 0), Vector(0, 1), 3)
print(list02)
# 练习2：在二维列表中，获取23位置向左2个元素
list03 = DoubleListHelper.get_elements(list01, Vector(2, 3), Vector.left(), 2)
print(list03)
# 练习3：在二维列表中，获取02位置向下2个元素
list04 = DoubleListHelper.get_elements(list01, Vector(0, 2), Vector.down(), 2)
print(list04)
# 练习4：在二维列表中，获取20位置右上2个元素
list05 = DoubleListHelper.get_elements(list01, Vector(2, 0), Vector.right_up(), 2)
print(list05)