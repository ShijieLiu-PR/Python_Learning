# 练习7：累加1-100之间能被3整除的整数和
sum = 0
for item in range(1, 101, 1):
    if item % 3 == 0:
        sum += item
print("sum = " + str(sum))

sum = 0
for item in range(1,101,1):
    if item % 3 != 0:
        continue
    sum += item
print("sum = " + str(sum))