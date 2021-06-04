"""
    模型定义
    1. 定义地图类
    2. 定义方向类
"""


class Map:
    """
        地图类定义
    """

    def __init__(self, row=4, col=4):
        self.__pos_list = []
        self.row = row
        self.col = col

    @property
    def row(self):
        return self.__row

    @row.setter
    def row(self, value):
        self.__row = value

    @property
    def col(self):
        return self.__col

    @col.setter
    def col(self, value):
        self.__col = value

    def get_element(self, row, col):
        return self.__pos_list[row][col]

    def init_map(self):
        for r in range(self.row):
            self.__pos_list.append([])
            for c in range(self.col):
                self.__pos_list[r].append(0)

    def print_map(self):
        for r in range(self.row):
            for c in range(self.col):
                print(self.__pos_list[r][c], end="  ")
            print()


class Dir:
    """
        定义方向类
    """
    left = 0
    right = 1
    up = 2
    down = 3


class Position:
    """
        位置类
    """
    def __init__(self, row, col):
        self.row = row
        self.col = col

    @property
    def row(self):
        return self.__row

    @row.setter
    def row(self, value):
        self.__row = value

    @property
    def col(self):
        return self.__col

    @col.setter
    def col(self, value):
        self.__col = value







if __name__ == "__main__":
    map = Map(4, 4)
    map.init_map()
    map.print_map()
    print(Dir.left)
    print(Dir.right)