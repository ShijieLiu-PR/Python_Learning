# 练习6：写一个函数，判断队列中是否具有相同元素。
def hold_same_element(list01):
    for i in range(len(list01)-1):
        for j in range(i+1,len(list01)):
            if list01[i] == list01[j]:
                return True
    return False

res = hold_same_element([1,2,3,4,5,6])
print(res)


# 练习7：写一个函数，根据月份判断季节。
def season(month):
    if month < 1 or month > 12:
        return "error"
    elif month < 4:
        return "Spring"
    elif month < 7:
        return "Summer"
    elif month < 10:
        return "Autumn"
    else:
        return "Winter"

print(  season(10))