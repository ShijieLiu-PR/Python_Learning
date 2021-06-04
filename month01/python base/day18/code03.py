"""
    装饰器
        --闭包的应用

"""
#
#
# def say_hello():
#     print("hello")
#
# def say_goodbye():
#     print("goodbye")

# 需求：在两个方法实现的功能基础上，增加新功能：打印方法名称。
# 缺点：代码重复
# 解决：提取打印方法名称的功能

def say_hello():
    print(say_hello.__name__)
    print("hello")


def say_goodbye():
    print(say_goodbye.__name__)
    print("goodbye")

say_hello()
say_goodbye()
