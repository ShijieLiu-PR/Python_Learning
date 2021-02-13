# 练习6：随机加法考试，在控制台中获取两个数字的相加结果，如果输入正确，成绩加10分，反之扣5分，总共5道题。
import random
score = 0
for item in range(5):
    num01 = random.randint(1,100)
    num02 = random.randint(1,100)
    result = int(input(str(num01) + " + " + str(num02) + " = "))
    if result == num01 + num02:
        score += 10
    else:
        score -= 5
print("Your score is:" + str(score))

