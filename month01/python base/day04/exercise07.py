# 练习7：在控制台中输入学生姓名，要求姓名不能重复，如果录入esc，则停止录入，打印每个学生姓名。
# stu_list = list()
# count = 0
# while True:
#     name = input("请输入第%d个学生姓名："%(count+1))
#     if name == "esc":
#         break
#     elif name not in stu_list:
#             stu_list.append(name)
#             count += 1
#     else:
#         None
# print(stu_list)

# 找出最大值
list01 = [45,12,53,78,11,23,19,59]
max_val = list01[0]
for item in range(1,len(list01),1):
    if max_val < list01[item]:
        max_val = list01[item]
print("最大值是%d"%(max_val))

for item in list01:
    print(item)