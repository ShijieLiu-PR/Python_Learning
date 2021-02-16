"""
    4.在控制台中录入5个学生信息（姓名/年龄/性别），用什么数据结果保存比较好？
    推荐：列表中嵌套字典
    [
       {
         "name":xx,
         "age":xx,
         "sex":xx,
       }
       ...
    ]
"""
list01 = []
dic01 = {}
for i in range(3):
    name = input("请输入第%d个学生姓名："%(i+1))
    dic01["name"] = name
    age = int(input("请输入第%d个学生年龄："%(i+1)))
    dic01["age"] = age
    sex = input("请输入第%d个学生性别："%(i+1))
    dic01["sex"] = sex
    list01.append(dic01)

print(list01)
