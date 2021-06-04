from Game2048.GameCoreController import *
import os


class GameView:
    def __init__(self):
        self.controller = GameCoreController()

    def print_map(self):
        for row in range(len(self.controller.game_model.core_list)):
            for col in range(len(self.controller.game_model.core_list[row])):
                print(self.controller.game_model.core_list[row][col], end="  ")
            print("")


gv = GameView()
gv.controller.reset_game_model()
gv.controller.gen_random_number()
gv.controller.gen_random_number()
while True:
    gv.print_map()
    key = input("").capitalize()
    if key == "A":
        gv.controller.move_left()
        gv.controller.gen_random_number()
    elif key == "D":
        gv.controller.move_right()
        gv.controller.gen_random_number()
    elif key == "W":
        gv.controller.move_up()
        gv.controller.gen_random_number()
    elif key == "S":
        gv.controller.move_down()
        gv.controller.gen_random_number()
    elif key == "E":
        break


