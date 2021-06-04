# 练习：参照下列代码，实现对技能列表的查找

from common.custom_list_tools import ListHelper
list01 = [45, 12, 6, 22, 56]
# for val in ListHelper.find_all(list01, lambda item: item > 20):
#     print(val)

#
# for val in ListHelper.find_all(list01, lambda item: item >30 and item%2 == 0):
#     print(val)

for val in ListHelper.find_all(list01, lambda item: item > 30 and item %2 != 0):
    print(val)