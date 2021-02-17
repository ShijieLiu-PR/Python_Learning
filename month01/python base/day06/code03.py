"""
    for for
"""
"""
    *****
    *****
    *****
"""
for row in range(3):
    for col in range(5):
        print("*",end = "")
    print()

for row in range(4):
    for col in range(6):
        if row % 2 == 0:
            print("*",end="")
        else:
            print("#",end="")
    print()

for row in range(4):
    for col in range(row+1):
        print("#",end="")
    print()

"""
    列表中是否具有相同元素[1,4,7,4,8,0,6]
    核心：所有元素间两两比较
    思想：取出第一个元素，与后面进行比较....
    
"""
list01 = [1,4,7,5,8,0,6]
result = False
for i in range(len(list01)-1):
    for j in range(i+1,len(list01),1):
        if list01[i] == list01[j]:
            result = True
            break
print(result)

"""
    对列表进行排序：[1,4,7,5,8,0,6]
    核心：两两元素进行比较。
"""
list02 = [1, 4, 7, 5, 8, 0, 6]
for i in range(len(list02)-1):
    for j in range(i+1, len(list02), 1):
        if list02[i] > list02[j]:
            list02[i], list02[j] = list02[j], list02[i]
print(list02)