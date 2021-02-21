""""""
"""
    内存图1.0
"""
def fun01(num01):
    num01 = 2
    print("num01:"+str(num01))

number01 = 1



# 调用方法，在内存中开辟空间（栈帧）
#栈帧中定义该方法内部创建的变量
#方法执行完毕后，栈帧立即释放
fun01(number01)
print("number01:"+str(number01))


"""
    内存图2.0
"""


def fun02(list_target):
    list_target[0] = 2000
    print("list_target[0]:" + str(list_target[0]))
list_number = [1, 2, 3, 4]
fun02(list_number)
print("list_number[0]:" + str(list_number[0]))