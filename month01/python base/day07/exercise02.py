# 练习2：统计一个方法的调用次数
count_fun01 = 0


def fun01():
    global count_fun01
    count_fun01 +=1



for i in range(11):
    fun01()
print(count_fun01)