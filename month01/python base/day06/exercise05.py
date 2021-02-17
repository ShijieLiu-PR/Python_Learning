# 练习5：在控制台中显示直角三角形的函数。


def triangle(side,char):
    """
    在控制台中打印直角三角形。
    :param side: 三角形的边长
    :param char: 三角形的字符。
    :return: 无
    """
    for i in range(side):
        for j in range(i+1):
            print(char, end = "")
        print()

triangle(4,"^")
