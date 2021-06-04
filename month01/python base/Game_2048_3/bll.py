"""
    业务逻辑层
"""
import model
import random

class GameController:
    """
        逻辑控制类
    """
    def __init__(self):
        self.map_list = []
        self.zero_pos_list = []

    def init_map(self):
        self.__map_list = [
            [0]*4,
            [0]*4,
            [0]*4,
            [0]*4,
        ]

    @property
    def map_list(self):
        return self.__map_list

    @map_list.setter
    def map_list(self, value):
        self.__map_list = value

    @property
    def zero_pos_list(self):
        return self.__zero_pos_list

    @zero_pos_list.setter
    def zero_pos_list(self, value):
        self.__zero_pos_list = value

    def __update_zero_pos_list(self):
        self.__zero_pos_list = []
        for r in range(len(self.__map_list)):
            for c in range(len(self.__map_list[r])):
                if self.__map_list[r][c] == 0:
                    self.__zero_pos_list.append(model.Position(r, c))

    def gen_random_value(self):
        self.__update_zero_pos_list()
        random_pos = random.choice(self.__zero_pos_list)
        random_val = 4 if random.randint(1, 10) > 9 else 2
        self.__map_list[random_pos.row][random_pos.col] = random_val
        self.__zero_pos_list.remove(random_pos)

    def __move_to_end(self):
        for r in range(len(self.__map_list)):
            for c in range(len(self.__map_list[r])-1, -1, -1):
                if self.__map_list[r][c] == 0:
                    del self.__map_list[r][c]
                    self.__map_list[r].append(0)

    def __merge_adjacent(self):
        for r in range(len(self.__map_list)):
            for c in range(len(self.__map_list[r])-1):
                if self.__map_list[r][c] == self.__map_list[r][c+1]:
                    self.__map_list[r][c] *= 2
                    self.__map_list[r][c+1] = 0
                    break

    def __reverse_row(self):
        for r in range(len(self.__map_list)):
            for c in range(len(self.__map_list[r])//2):
                self.__map_list[r][c], self.__map_list[r][len(self.__map_list[r])-1-c] = \
                    self.__map_list[r][len(self.__map_list[r])-1-c],  self.__map_list[r][c]

    def __switch_row_col(self):
        for r in range(len(self.__map_list)):
            for c in range(r, len(self.__map_list[r])):
                self.__map_list[r][c], self.__map_list[c][r] = self.__map_list[c][r], self.__map_list[r][c]

    def __move_left(self):
        self.__move_to_end()
        self.__merge_adjacent()
        self.__move_to_end()

    def __move_right(self):
        self.__reverse_row()
        self.__move_left()
        self.__reverse_row()

    def __move_up(self):
        self.__switch_row_col()
        self.__move_left()
        self.__switch_row_col()

    def __move_down(self):
        self.__switch_row_col()
        self.__move_right()
        self.__switch_row_col()

    def move(self, dir):
        if dir == model.Dir.left:
            self.__move_left()
        elif dir == model.Dir.right:
            self.__move_right()
        elif dir == model.Dir.up:
            self.__move_up()
        elif dir == model.Dir.down:
            self.__move_down()
        else:
            pass

    def __adjacent_equal_row(self):
        for r in range(len(self.map_list)):
            for c in range(len(self.map_list[r])-1):
                if self.map_list[r][c] == self.map_list[r][c+1] and self.map_list[r][c] != 0:
                    return True
        return False

    def __adjacent_equal_col(self):
        for r in range(len(self.map_list)-1):
            for c in range(len(self.map_list[r])):
                if self.map_list[r][c] == self.map_list[r+1][c] and self.map_list[r][c] != 0:
                    return True
        return False

    def adjacent_equal(self):
        return self.__adjacent_equal_row() or self.__adjacent_equal_col()


