"""
    2048核心算法
"""

# 练习1：定义函数，将0元素移动到末尾
# [2,0,2,0] -> [2,2,0,0]
# [0,2,2,0] -> [2,2,0,0]
# [0,4,2,0] -> [4,2,0,0]
#10:18
"""
def zero_to_end(list_target):
    
       # 1.将传入的列表中非0元素，拷贝到新列表中。
       # [2,0,2,0] --> [2,2] --> [2,2,0,0]
       # 2.根据为0元素数量，在新列表中添加0元素
   
    #new_list = []
    # for item in list_target:
    #     if item != 0:
    #         new_list.append(item)
    # for i in range(len(list_target) - len(new_list)):
    #     new_list.append(0)
    new_list = [item for item in list_target if item != 0]
    new_list += [0] * list_target.count(0)
    #3.将新列表中的元素赋值传入的列表
    list_target[:] = new_list
"""
# 删除0元素


def zero_to_end(list_target):
    for i in range(len(list_target)-1, -1, -1):
        if list_target[i] == 0:
            del list_target[i]
            list_target.append(0)



# 练习2：定义合并函数
# [2,2,0,0]  -> [4,0,0,0]
# [2,0,2,0]  -> [4,0,0,0]
# [2,2,2,0]  -> [4,2,0,0]



def merge(list_target):
    zero_to_end(list_target)
    for i in range(len(list_target) - 1):
        if list_target[i] == list_target[i+1] and list_target[i] != 0:
            list_target[i+1] += list_target[i]
            list_target[i] = 0
    zero_to_end(list_target)


# 练习3：将二维列表以表格的格式显示在控制台中。
def print_map(list_target):
    for i in list_target:
        for j in i:
            print(str(j) + " ",end="")
        print()


# 练习4：定义向左移动函数。
"""
    [2,0,0,2]->[4,0,0,0]
    [2,2,0,0]->[4,0,0,0]
    [2,0,4,4]->[2,8,0,0]
    [4,0,0,2]->[4,2,0,0]

"""


def move_left(list_target):
    for item in list_target:
        zero_to_end(item)
        merge(item)


def move_right(list_target):
    for i in range(len(list_target)):
        zero_to_end((list_target[i]))
        merge(list_target[i])
        list_target[i] = list_target[i][::-1]


# 定义转置函数
def swap_row_col(list_target):
    for i in range(len(list_target)):
        for j in range(i, len(list_target)):
            list_target[i][j], list_target[j][i] = list_target[j][i], list_target[i][j]


# 作业1：定义向上移动函数
def move_up(list_target):
    swap_row_col(list_target)
    move_left(list_target)
    swap_row_col(list_target)


# 作业2：定义向下移动函数
def move_down(list_target):
    swap_row_col(list_target)
    move_right(list_target)
    swap_row_col(list_target)


list01 = [2, 2, 4, 0]
list02 = [
    [2,0,0,2],
    [2,2,0,0],
    [2,0,4,4],
    [4,0,0,2],
]
move_down(list02)
print_map(list02)