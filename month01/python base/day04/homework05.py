# 5.一注彩票7个球，其中前6个是红球1-33之间的数字，且不能重复，最后一个是蓝球，1-16之间的整数。
#     a.在控制台中购买彩票
#     b.随机产生一注彩票
import random
list01 = []
count = 0
while True:
    count += 1
    operation = input("请输入操作码（a.在控制台中购买彩票；b.随机产生一注彩票；q.退出）:")
    if operation == "b":
        list01 = []
        random.seed(count)
        while len(list01) < 7:
            if len(list01) == 6:
                ran = random.randint(1, 16)
                list01.append(ran)
            else:
                ran = random.randint(1, 33)
                if ran not in list01:
                    list01.append(ran)
        print(list01)
    elif operation == "a":
        list01 = []
        while len(list01) < 7:
            if len(list01) == 6:
                ran = int(input("请输入第%d个号码(1-16)："%(len(list01)+1)))
                if 1<=ran<=16:
                    list01.append(ran)
            else:
                ran = int(input("请输入第%d个号码(1-33)："%(len(list01)+1)))
                if (1<= ran <= 33) and (ran not in list01):
                    list01.append(ran)
        print(list01)
    elif operation == "q":
        break
    else:
        print("error!")
