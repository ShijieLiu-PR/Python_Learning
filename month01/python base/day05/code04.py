"""
    字典dic
"""
# 1. 创建字典
d01 = {"key":"value"}
d02 = {}
d03 = dict()

d01 = {"a":"A", "b":"B"}
#d01 = dict("ab")  分不清键值
d01 = dict([(1,2),(3,4)])
print(d01)

# 第一次增加，第二次修改
d01["c"] = "C"
print(d01)

# 读取元素不存在，则异常。
print(d01["c"])

# 获取字典中所有元素
# for key in d01:
#     print(key)
# for item in d01.items():
#     print(item)
# for key in d01.keys():
#     print(key)
#
# for key,value in d01.items():
#     print(key)
#     print(value)

for value in d01.values():
    print(value)