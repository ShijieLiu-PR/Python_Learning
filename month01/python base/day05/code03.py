"""
    元组tuple
"""
# 1.创建空元组
t01 = ()
t02 = tuple()

# 2.创建具有默认值的元组
t01 = (1,2,3)
t02 = tuple("abcd")
print(t01)
print(t02)
t03 = (1,2,[3,4])
print(t03)
print(t03[2][1])

# 3.修改
t03[2][1] = 5
print(t03)

# 4.获取元素(索引和切片)
print(t03[:3:])
for item in t03:
    print(item)

for i in range(len(t03)-1,-1,-1):
    print(t03[i])

t02 = ("a","b")
l02 = ["a","b"]
t03 = t02
l03 = l02
print("id(t02)="+str(id(t02)))
print("id(t03)="+str(id(t03)))
t02 += ("c","d") #创建了新元组，改变了t02的存储地址
l02 += ["c","d"] #修改的是元素
print("t02="+str(t02))
print("t03="+str(t03))
print("l02="+str(l02))
print("l03="+str(l03))

print("id(l02)="+str(id(l02)))
print("id(l03)="+str(id(l03)))
print("id(t02)="+str(id(t02)))
print("id(t03)="+str(id(t03)))

# 如果元组只有一个元素，必须多写一个逗号，否则视为普通对象，而不是元组。例如 t04 =(1,)
t04 = (1,)
print(t04)