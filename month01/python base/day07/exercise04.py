# 练习4：定义函数，整数相加的函数
def add(*args):
    for item in args:
        print(item)
    return sum(args)
print(add(1,2,3,4))

