"""
    函数式编程
"""

#
# def fun01():
#     print("fun01执行了。")
#
# a = fun01()
#
# # 将方法赋值给变量a，没有执行fun01
# a = fun01
# # 调用变量a，间接执行函数fun01
# a()
# # 将方法fun01作为方法的参数func进行传递
# def  fun02(func):
#     print("fun02执行了。")
#     # 对于fun02的定义者而言，不知道也不需要知道func的具体逻辑。
#     func()
#
# fun02(fun01)


list01 = [1,2,33,4,45,6]
def find_demo01(target):
    for item in target:
        if item > 5:
            yield item


# 提取相同点
def find_demo01(target, condition):
    for item in target:
        if condition(item):
            yield item


# 提取不同点
def condition01(item):
    return item > 5

def condition02(item):
    return item % 2 != 0

def condition03(item):
    return item < 3


for item in find_demo01(list01, condition03):
    print(item)