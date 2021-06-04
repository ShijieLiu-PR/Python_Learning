"""

"""

list01 = ["a", "b", "c"]
for item in list01:
    print(item)
print(enumerate(list01))

for index, element in enumerate(list01):
    print(index,element)

#参照上午代码，自定义my_enumerate

def my_enumerate(target):
    res = list()
    for i in range(len(target)):
        res.append((i, target[i]))
    return res


def my_enumerate2(target):
    i = 0
    for ele in target:
        yield i, ele
        i += 1


for index, element in my_enumerate2(list01):
    print(index, element)


list02 = ["A", "B", "C"]
list03 = ["张三丰", "张无忌", "赵敏", "周芷若"]
# for item in zip(list02, list03):
#     print(item)


# 参照上述代码，自定义函数my_zip
def my_zip(target1, target2):
    for i in range(min(len(target1), len(target2))):
        yield target1[i], target2[i]
    print(min(len(target1), len(target2)))

for item in my_zip(list02, list03):
    print(item)