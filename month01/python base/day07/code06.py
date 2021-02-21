"""
    形参传递方式
        默认形参
        位置形参：
            --星号元组形参：位置实参数量无限
        命名关键字形参：要求必须使用关键字实参
            --双星号字典形参：关键字参数无限
    学习目标：会调用其他人写的函数。
"""
# 位置参数
def fun01(a,b,c):
    pass

# 星号元组形参
# 对于方法内部而言，就是元组，对于调用者而言，可以传递数量无限的位置实参。
def fun02(*a):
    print(a)

fun02()
fun02(1)
fun02(1,2,3,4)

# 命名关键字形参
def fun03(*a,b):
    print(a)
    print(b)
    pass

fun03(1,2,3,4,b=5)
# 双星号字典形参
# 对方法内部而言，就是字典，对调用者而言，可以传递数量无限的关键字。
def fun05(**kwarg):
    print(kwarg)

fun05(a =1, b=2)

# 调用
def fun06(*args,**kwargs):
    print(args)
    print(kwargs)
print(fun06(1,2,3, a = 1,b=2))

def fun07(a,b,*args,c,d,**kwargs):
    print(a)
    print(b)
    print(args)
    print(c)
    print(d)
    print(kwargs)

fun07(1,2,3,4,5,c=6,d=7,e=8,f=9)

print(1,2,3,sep = "---",end="abc")
print(1,2,3,sep = "---",end="abc")