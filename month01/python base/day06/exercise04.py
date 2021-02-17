# 练习4：写一个函数，在控制台中打印矩形，可以实现任意的边长。
def rectangle(side):
    """

    :param side:
    :return:
    """
    for i in range(side):
        for j in range(side):
            print("*", end="")
        print()

rectangle(4)
rectangle(10)