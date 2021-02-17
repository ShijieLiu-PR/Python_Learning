"""
    day05复习
    容器
        字符串：不可变的字符序列
        列表：变量  可变 内存中有预留空间  序列
        元组：变量  不可变  序列
        字典：键值对  可变的  内存中有预留空间   映射
        集合/固定集合

"""

list01 = [1,2,1]
list01.append(3)
print(list01)
list01.remove(1)
print(list01)

# 元组
t01 = (1,)
t02 = tuple()

# 字典
d01 = {"a":2,"b":1,"c":2}
print(d01.values())
for k,v in d01.items():
    print(str(k) + str(v))
for key in d01:
    print(key)
for value in d01.values():
    print(value)