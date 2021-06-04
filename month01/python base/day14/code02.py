"""
    异常处理
"""

def div_apple(apple_count):
    # 分苹果
    person_count = int(input("please input person count:"))  # ValueError
    result = apple_count / person_count   # ZeroDivisionError
    print("Each person gets %d apples!" % result)

# 缺点：不能根据具体错误，做出相应处理逻辑。
try:
    div_apple(5)
except ValueError as e:
    print("输入的人数有误。")
    print(e.args)
except ZeroDivisionError:
    print("输入的人数不能为0.")
except Exception:
    print("未知类型的错误。")
else:
    print("没有发生异常。")
finally:
    print("无论是否有异常，都会执行的部分。")
print("following logics。。。")