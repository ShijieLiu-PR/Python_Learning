from Game2048.GameModel import *
import random


class GameCoreController:
    def __init__(self):
        self.game_model = GameModel()
        self.zero_pos_list = list()

    def reset_game_model(self):
        for row in range(4):
            for col in range(4):
                self.game_model.core_list[row][col] = 0

    def zero_to_end(self):
        for element in self.game_model.core_list:
            for i in range(len(element) - 1, -1, -1):
                if element[i] == 0:
                    del element[i]
                    element.append(0)

    def merge_adjacent(self):
        for element in self.game_model.core_list:
            for i in range(len(element)):
                if element[i] != 0 and element[i] == element[i+1]:
                    element[i] *= 2
                    element[i+1] = 0
                    break

    def print_map(self):
        for item in self.game_model.core_list:
            print(item)
        print("-----------------------------")

    def reverse_row(self):
        new_list = []
        for element in self.game_model.core_list:
            new_list.append(element[::-1])
        self.game_model.core_list = new_list

    def exchange_row_col(self):
        for i in range(len(self.game_model.core_list)):
            for j in range(i+1, len(self.game_model.core_list[i])):
                self.game_model.core_list[i][j], self.game_model.core_list[j][i] = self.game_model.core_list[j][i], self.game_model.core_list[i][j]

    def move_left(self):
        self.zero_to_end()
        self.merge_adjacent()
        self.zero_to_end()

    def move_right(self):
        self.reverse_row()
        self.move_left()
        self.reverse_row()

    def move_up(self):
        self.exchange_row_col()
        self.move_left()
        self.exchange_row_col()

    def move_down(self):
        self.exchange_row_col()
        self.move_right()
        self.exchange_row_col()

    def get_zero_index(self):
        self.zero_pos_list = list()
        for i in range(len(self.game_model.core_list)):
            for j in range(len(self.game_model.core_list[i])):
                if self.game_model.core_list[i][j] == 0:
                    self.zero_pos_list.append((i, j))

    def gen_random_number(self):
        self.get_zero_index()
        pos = random.randint(0, len(self.zero_pos_list)-1)
        number = random.choices((2, 4), (1, 9))[0]
        row = self.zero_pos_list[pos][0]
        col = self.zero_pos_list[pos][1]
        self.game_model.core_list[row][col] = number

# below is test code
if __name__ == "__main__":
    gc = GameCoreController()
    gc.reset_game_model()
    gc.print_map()
    gc.move_left()
    gc.print_map()
    gc.gen_random_number()
    gc.print_map()
