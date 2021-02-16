# 练习1：使用range生成1--10之间的数字，存入list01中，
#       使用列表推导式，将list01中所有奇数存入到list02，
#       将所有偶数存入到list03中，将大于3的存入到list04中

list01 = list(range(1,11,1))
print(list01)
list02 = [item for item in list01 if item % 2 != 0]
list03 = [item for item in list01 if item % 2 == 0]
list04 = [item for item in list01 if item > 3]
print("list02="+str(list02))
print("list03="+str(list03))
print("list04="+str(list04))