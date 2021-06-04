"""
    可迭代对象：具有__iter__方法，可以返回迭代器的对象。
"""
#
list01 = [2, 45, 25, 22]
# for item in list01:
#     print(item)

# for循环原理
# 1.获取迭代器对象
# 2.循环迭代（调用迭代器__next__方法）
# 3.捕获StopIteration异常
#1. 获取迭代器对象
iterator = list01.__iter__()
while True:
    try:
        # 2.获取下一个元素
        item = iterator.__next__()
    except:
        break
    print(item)