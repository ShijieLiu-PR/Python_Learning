"""
    列表推导式嵌套
"""
list01 = ["a", "b", "c"]
list02 = ["A", "B", "C"]
list03 = list()
# for i in list01:
#     for j in list02:
#         print(i+j)
#         list03.append(i+j)
# print(list03)

list04 = [i + j for i in list01 for j in list02]
print(list04)