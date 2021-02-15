"""
    列表
"""
#1.创建空列表
list01 = []
list01 = list()
#2.创建具有默认值的列表[元素1，元素2，元素3..] list(可迭代对象)
list02 = [1,True,1.2]
list02 = list("abcd")
list02 = list(range(5))
print(list02)

#3.添加元素
#append在末尾追加
list02.append("q")
list02.append("t")
print(list02)
#insert插入（索引，元素)
list02.insert(1,"x")
print(list02)

#4.删除元素，移除指定的元素
list02.remove(2)
print(list02)
#删除指定索引的元素
del list02[1]
print(list02)

#5.获取元素（索引，切片）
print(list02[3])
print(list02[:3])
list02[:3] = ["a","b","c","d","e"]
list02[:3] = ["a"]
print(list02)

#6.遍历元素
# for item in range(len(list02)):
#     print(list02[item])
# for item in range(0,len(list02),2):
#     print(list02[item])
# for item in range(len(list02)-1,-1,-1):
#     print(list02[item])
for item in range(-1,-len(list02)-1,-1):
    print(list02[item])