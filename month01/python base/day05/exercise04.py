# 练习4：在控制台中输入季度，打印该季度的月份。
quarter = int(input("请输入季度："))
seasons = {
    1:"有1,2,3月",
    2:"有4,5,6月",
    3:"有7,8,9月",
    4:"有10,11,12月"
}
dict01 = {1:(1,2,3),2:(4,5,6),3:(7,8,9),4:(10,11,12)}
print(dict01[quarter])
print("-".join(str(dict01[quarter])))

print(seasons[quarter])


list01 = [1,2,3]
list02 = [str(item) for item in list01]
print("-".join(list02))

print(seasons)
del seasons[2]
print(seasons)