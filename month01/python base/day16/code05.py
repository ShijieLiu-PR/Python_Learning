"""
    lambda 表达式(匿名方法)
    语法：
    lambda 参数：方法体
"""

def fun01():
    print("我是普通方法。")

a01 = lambda : print("我是lambda方法")
a01()



def fun02(a):
    print("我是普通方法，参数是", a)

a02 = lambda a :print("我是lambda方法，参数是", a)
a02(5000)



def fun03():
    return True

a03 = lambda : True
print(a03())


# 应用
from common.custom_list_tools import ListHelper
list01 = [1,2,33,4,45,6]

# 提取不同点
def condition01(item):
    return item > 5

def condition02(item):
    return item % 2 != 0

def condition03(item):
    return item < 3


for item in ListHelper.find_all(list01, condition01):
    print(item)

for item in ListHelper.find_all(list01, lambda item : item < 3):
    print(item)