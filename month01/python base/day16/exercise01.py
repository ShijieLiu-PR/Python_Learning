# 练习1：将以下代码，不变的步伐提取到一个方法find_all中，
# 将变化点，提取到不同方法中，
# 再实现原有功能。

list01 = [3,45,5,6,11]
def find_demo02(target):
    for item in target:
        if item.cd == 0:
            yield item


def find_demo03(target):
    for item in target:
        if item.atk > 5:
            yield item


def find_demo04(target):
    for item in target:
        if item.atk > 10 and item.costSP == 0:
            yield item


# 提取共同点

def find_all(target, condition):
    for item in target:
        if condition(item):
            yield item


# 提取变化点

def condition01(item):
    return item.cd == 0

def condition02(item):
    return item.atk > 5

def condition03(item):
    return item.atk > 10 and item.costSP == 0


from common.custom_list_tools import ListHelper
ListHelper.find_all(list01,condition02())
