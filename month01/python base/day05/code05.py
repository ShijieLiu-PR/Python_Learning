"""
    字典推导式
"""
# key:数字     value：数字平方

dic01 = {}
for item in range(1,10,1):
    dic01[item] = item**2
print(dic01)

dic02 = {item:item**2 for item in range(1,10,1)}
print(dic02)

dic03 = {item:item**2 for item in range(1,10,1) if item % 2 == 0}
print(dic03)
