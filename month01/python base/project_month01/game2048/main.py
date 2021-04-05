"""
    程序入口
"""

from ui import *
from bll import *
from model import *
# 从当前模块运行，执行程序逻辑
if __name__ == "__main__":
    stu_manager = StudentManagerController()
    view = StudentManagerView()
    view.main()
