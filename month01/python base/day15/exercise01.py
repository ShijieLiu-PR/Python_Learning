# 练习1：（"悟空","八戒","沙僧","唐僧"），使用while + 迭代器 获取元组所有元素。

tuple01 = {"悟空", "八戒", "沙僧", "唐僧"}
iterator = tuple01.__iter__()
while True:
    try:
        item = iterator.__next__()
    except:
        break
    print(item)