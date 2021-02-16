"""
5.扩展练习：
    猜拳
    规则：系统随机出拳，在控制台中循环猜测
    提示：将胜利的策略存入容器
    （
        （"石头","剪刀"），
        （“剪刀”，“布”）,
        （“布”，“石头”）
    ）
    将用户猜的拳与系统出的拳形成一个元组

"""
import random
fist_list = ["剪刀","石头","布"]
victory = (("石头","剪刀"),("剪刀","布"),("布","石头"))
while True:
    pc_fist =fist_list[random.randint(0,2)]
    my_fist = fist_list[int(input("请输入你的拳头（0-剪刀，1-石头，2-布，3-退出游戏）："))]
    if my_fist == 3:
        break
    print("pc_fist:%s"%(pc_fist))
    print("my_fist:%s"%(my_fist))
    if my_fist == pc_fist:
        print("平局！")
    elif (my_fist,pc_fist) in victory:
        print("我赢了，哈哈！")
    else:
        print("我输了！")
