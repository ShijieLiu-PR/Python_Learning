# 练习7：["张三丰","无忌","赵敏"]
# [101,102,103]
# （1）根据两个列表形成一个字典：key姓名，value房间号
# （2）将字典的键与值进行翻转，即：key房间号，value姓名
name_list = ["张三丰","无忌","赵敏"]
room_list = [101,102,103]
dic01 = {name_list[item]:room_list[item] for item in range(len(name_list))}
print(dic01)
dic02 = {value:key for key,value in dic01.items()}
print(dic02)