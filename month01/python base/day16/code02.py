"""
    生成器表达式
"""

list01 = [2,3,4,6]
result = [ x**2 for x in list01]
print(result)

result = (x**2 for x in list01)
for item in result:
    print(item)


list02 = [2,3,4,6]
# 练习：使用列表推导式与生成器表达式，获取列表list02中大于3的数据。
result01 = [item for item in list02 if item > 3]
print(result01)
result02 = (item for item in list02 if item > 3)
for item in result02:
    print(item)

