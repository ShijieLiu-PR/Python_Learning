"""
    ui界面
    表示层
"""
from bll import GameCoreController
from model import Direction
import os


class GameConsoleView:
    """
    控制台视图
    """
    def __init__(self):
        self.__controller = GameCoreController()

    def start(self):
        """
        游戏开始
        :return:
        """
        self.__controller.gen_random_number()
        self.__controller.gen_random_number()
        self.print_map()

    def print_map(self):
        """
        打印界面
        :return:
        """
        print("-----------------------")
        for r in range(len(self.__controller.map)):
            for c in range(len(self.__controller.map[r])):
                print(self.__controller.map[r][c], end="  ")
            print()

    def update(self):
        """
            更新逻辑
        :return:
        """
        while True:
            self.move_map()
            if self.__controller.is_change:
                self.__controller.gen_random_number()
            os.system("cls")
            self.print_map()

    def move_map(self):
        dir = input("请输入移动方向(WSAD):").upper()
        if dir == "W":
            self.__controller.move(Direction.up)
        elif dir == "S":
            self.__controller.move(Direction.down)
        elif dir == "A":
            self.__controller.move(Direction.left)
        elif dir == "D":
            self.__controller.move(Direction.right)
        else:
            pass

