"""
    业务逻辑层
"""


import random
from model import Location
import copy

class GameCoreController:
    """
        游戏核心逻辑控制
    """
    def __init__(self):
        self.__map = [
            [0]*4,
            [0]*4,
            [0]*4,
            [0]*4,
        ]
        self.__list_empty_location = []
        self.is_change = False

    @property
    def map(self):
        return self.__map

    @map.setter
    def map(self, value):
        self.__map = value

    @property
    def is_change(self):
        return self.__is_change

    @is_change.setter
    def is_change(self, value):
        self.__is_change = value

    def zero_to_end(self):
        for element in self.map:
            for i in range(len(element) - 1, -1, -1):
                if element[i] == 0:
                    del element[i]
                    element.append(0)

    def merge_adjacent(self):
        for element in self.map:
            for i in range(len(element)):
                if element[i] != 0 and element[i] == element[i + 1]:
                    element[i] *= 2
                    element[i + 1] = 0
                    break

    def __reverse_row(self):
        new_list = []
        for element in self.map:
            new_list.append(element[::-1])
        self.map = new_list

    def __exchange_row_col(self):
        for i in range(len(self.map)):
            for j in range(i+1, len(self.map[i])):
                self.map[i][j], self.map[j][i] = self.map[j][i], self.map[i][j]

    def move(self, dir):
        self.is_change = False
        original_map = copy.deepcopy(self.__map)
        if dir == 0:
            self.__move_up()
        elif dir == 1:
            self.__move_down()
        elif dir == 2:
            self.__move_left()
        elif dir == 3:
            self.__move_right()
        else:
            pass
        self.is_change = self.__equal_map(original_map)

    def __equal_map(self, original):
        for r in range(4):
            for c in range(4):
                if original[r][c] != self.__map[r][c]:
                    return True

    def __move_left(self):
        self.zero_to_end()
        self.merge_adjacent()
        self.zero_to_end()

    def __move_right(self):
        self.__reverse_row()
        self.__move_left()
        self.__reverse_row()

    def __move_up(self):
        self.__exchange_row_col()
        self.__move_left()
        self.__exchange_row_col()

    def __move_down(self):
        self.__exchange_row_col()
        self.__move_right()
        self.__exchange_row_col()

    def __calculate_empty(self):
        self.__list_empty_location = []
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if self.map[i][j] == 0:
                    self.__list_empty_location.append(Location(i, j))

    def gen_random_number(self):
        self.__calculate_empty()
        if len(self.__list_empty_location) == 0:
            return 0
        # 从空位置中随机选择一个元素
        loc = random.choice(self.__list_empty_location)
        self.__map[loc.r_index][loc.c_index] = 2 if random.randint(1, 10) < 10 else 4
        self.__list_empty_location.remove(loc)

    def print_map(self):
        for item in self.map:
            print(item)
        print("-----------------------------")
