list01 = [1,2]
list02 = list01
# 改变的是列表的第一个元素的地址
list01[0] = 100
print(list02[0])

list01 = [1,2]
list02 = list01
list01 = [100]
print(list02[0])


# 第3张图
list01 = [1,2]
list02 = list01[:]
list01 = 100
print(list02[0])

# 4
list01 = [1,[2,3]]
list02 = list01.copy()
# 只拷贝一层
list01[1][0] = 200
print(list02[1][0])

import copy
list01 = [1,[2,3]]
list02 = copy.deepcopy(list01)
print(list01)
list01[1][0] = 10
print(list01)
print(list02)
