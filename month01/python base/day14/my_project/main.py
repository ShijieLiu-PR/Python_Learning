"""
练习1：目标 -- 在实际项目结构中，随心所欲地调用不同模块的成员。
    1.建相应的包与模块
    2.在相应模块找那个定义函数/类
    3.在main中调用skill_manager模块中的成员
    4.在skill_manager模块中，调用skill_deployer模块成员
    5.在skill_data模块中，调用list_helper模块成员。
        my_project/
            main.py
            common/
                __init__.py
                double_list_helper.py
                list_helper.py
            skill_system/
                __init__.py
                skill_data.py
                skill_deployer.py
                skill_manager.py
"""

import skill_system.skill_manager as sm
import sys

if __name__ == "__main__":
    print("hello world!")
    sm.fun01()

print(sys.path)
for item in sys.path:
    print(item)