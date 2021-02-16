"""
6.群讨论：
    讨论 == is 的区别。
    讨论列表中的元素如何根据条件批量删除，例如删除列表中[1,2,3,4,5,0,6,7]大于3的数。
"""
# ==判断两个变量的值是否相同
# is用来判断两个变量是否指向同一块区域，相当于判断id是否相等。
list01 = [1,2]
list02 = list01
list02 = list01[::]
print(list01 == list02)
print(list01 is list02)

print(id(list01))
print(id(list02))