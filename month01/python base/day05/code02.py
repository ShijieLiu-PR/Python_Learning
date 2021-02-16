"""
    列表推导式
"""
list01 = [3,5,6,7,9]
# 需求：创建新列表，每个元素是list01中的元素的平方
list02 = []
for item in list01:
    list02.append(item **2)
print(list02)

list03 = [item ** 2 for item in list01]
print(list03)

# 需求：创建新列表，如果元素是偶数，则将该元素的平方存入新列表
list04 = [item ** 2 for item in list01 if item % 2 != 0]
print(list04)