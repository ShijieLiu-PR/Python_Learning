"""
    游戏入口
"""
from ui import GameConsoleView
import os
if __name__ == "__main__":
    gcv = GameConsoleView()
    gcv.start()
    gcv.update()
