# 练习5：猜数字，产生1-100之间的随机数，让用户重复猜测，直到猜对为止。提示大了，小了，猜对了。最多只能猜10次
import random
ran = random.randint(1,100)
print(ran)
count = 0
while True:
    count += 1
    guess = int(input("请猜测(还能猜%s次)：" % (10-count)))
    if ran > guess:
        print("小了")
    elif ran < guess:
        print("大了")
    else:
        print("猜对了")
        break
    if count >= 10:
        break;

