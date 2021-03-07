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

    def fun01(self):
        pass

    def add_dir(self, ):
        pass

    # 类方法
    @classmethod
    def fun02(cls):
        pass

    # 静态方法：得不到对象地址，也得不到类地址
    @staticmethod
    def fun03(cls):
        pass


def get_elements(list_target, v_pos, v_dir, count):
    result = []
    # 位置 1 0  ->  方向 0 1
    for i in range(count):
        v_pos.x += v_dir.x
        v_pos.y += v_dir.y
        result.append(list_target[v_pos.x][v_pos.y])
    return result


list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"]
]

list02 = get_elements(list01, Vector(1, 0), Vector(0, 1), 3)
print(list02)
