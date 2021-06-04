# 练习2：{"张三丰":101, "张无忌":102, "赵敏":103}，不使用for循环，获取字典所有元素。

dict01 = {"张三丰":101, "张无忌":102, "赵敏":103}
iterator = dict01.__iter__()
while True:
    try:
        item = iterator.__next__()
    except:
        break
    print("%s = %d" % (item, dict01[item]))