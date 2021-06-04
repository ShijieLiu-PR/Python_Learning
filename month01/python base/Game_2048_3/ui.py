"""
    界面视图
"""
from bll import *
from model import *
from copy import *
import os


class View:
    def __init__(self):
        self.game_controller = GameController()

    def start(self):
        self.game_controller.init_map()
        self.game_controller.gen_random_value()
        self.game_controller.gen_random_value()
        self.print_map()

    def print_map(self):
        os.system("cls")
        for r in range(len(self.game_controller.map_list)):
            for c in range(len(self.game_controller.map_list[r])):
                print("%-4s" % self.game_controller.map_list[r][c], end="  ")
            print()

    def running(self):
        while True:
            user_input = View.get_input()
            if user_input is not None:
                original_map = deepcopy(self.game_controller.map_list)
                self.game_controller.move(user_input)
                if original_map != self.game_controller.map_list:
                    self.game_controller.gen_random_value()
            self.print_map()
            if len(self.game_controller.zero_pos_list) == 0 and not self.game_controller.adjacent_equal():
                print("Game Over!")
                break

    @staticmethod
    def get_input():
        res = input("请输入移动方向（左移：A，右移：D，上移：W，下移：S）：").upper()
        if res == "A":
            return Dir.left
        elif res == "D":
            return Dir.right
        elif res == "W":
            return Dir.up
        elif res == "S":
            return Dir.down
        else:
            return None


if __name__ == "__main__":
    view = View()
    view.start()
    view.print_map()
