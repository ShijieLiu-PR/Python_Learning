"""
    集合
"""
# 1.创建集合
s01 = set()
# 2.创建具有默认值的集合
s01 ={1,2,3,4,3}
print(s01)
# 3.其他容器变为集合
s02 = set("abcdefg")
print(s02)
s03 = set([1,7,56,8,7,8])
print(s03)
l02 = list(s03)
print(l02)
t02 = tuple(s03)
print(t02)
# 4.增加元素
s02.add("ssss")
print(s02)

# 5.删除元素
s02.remove("e") # 如果该元素不存在，则报错。
print(s02)
if 9 in s02:
    s02.remove(9)
# 两句话合成一句话
s02.discard("a")
print(s02)
# 6.获取所有元素
for item in s02:
    print(item)
# 7.计算
s03 = {1,2,3}
s04 = {2,3,4,5}
# 交集
s05 = s03 & s04
print(s05)
# 并集
s06 = s03 | s04
print(s06)
# 补集
s07 = s03 ^ s04
print(s07)
s08 = s03 - s04
print(s08)
s09 = s04 - s03
print(s09)

# 子集 超集
s06 = {1,2,3}
s07 = {1,2,4}
print(s07 < s06)

# 相同  不同
s08 = {1,2,3}
s09 = {1,2,3}
re = s08 == s09
print(re)