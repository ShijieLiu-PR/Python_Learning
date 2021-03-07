"""
    实参：
        --位置实参： fun(1,2,3)
            --序列实参
        --关键字实参：fun(a = 1, b = 2, c = 3)
            --字典实参

    形参：
        位置形参：
            --星号元组形参：无限位置
        关键字形参：
            --双星号字典形参：无限关键字
"""

def fun03(a,b,c):
    pass

fun03(b = 1, c = 2, a = 3)
list01 = [1,2,3]
fun03(*list01)
dict01 = {"a":1,"b":2,"c":3}
fun03(**dict01)

def fun04(*args,a,b,c):
    pass

def fun05(**kwargs):
    for k,v in kwargs.items():
        print(k,v,sep="=",end="\n")
fun05(**{"a":1,"b":2,"c":3})
list01 = [4,1,5,3,9]
list01.sort()
print(list01)