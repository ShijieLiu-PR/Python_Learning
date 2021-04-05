"""
    call module01
    模块调用
"""
# 导入方式1
# 导入模块名称
# 本质：将该模块作用域赋值给变量module01
# import module01
# import module01
# module01.fun01()
# mc01 = module01.MyClass01()
# mc01.fun02()

# 导入方式2
# 本质：将该模块指定成员 赋值给 fun01，MyClass
from module01 import fun01, MyClass01
fun01()
mc02 = MyClass01()
mc02.fun02()


# 导入方式3
from module01 import *
fun01()
mc02 = MyClass01()
mc02.fun02()

