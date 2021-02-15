# 4. 在控制台中录入一个整数，判断是否为素数（只能被1和自身整除的数）
num01 = int(input("Please input the number:"))
for item in range(2, num01, 1):
    if num01 % item == 0:
        break
if item + 1 == num01:
    print("Yes")
else:
    print("No")


count = 0
while count < 10:
    print(count)
    count += 1
    if count > 8:
        break
else:
    print("Done")