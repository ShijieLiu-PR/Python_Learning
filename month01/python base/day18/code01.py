"""
    外部嵌套作用域
"""

# 全局变量
g01 = 100
def fun01():
    # 局部变量L
    a = 1 # 局部变量L

    def fun02():
        b = 2 # fun02局部变量L
        nonlocal a #