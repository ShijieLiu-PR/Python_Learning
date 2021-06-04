# 练习3：定义方法，在控制台中获取成绩int（1-100之间）
# 要求：如果输入有误，重新输入：


class RangeError(Exception):
    def __init__(self, msg, code, value):
        super().__init__(msg)
        self.code = code
        self.value = value

def get_int():
    while True:
        input_string = input("请输入1-100之间的整数：")
        try:
            input_int = int(input_string)
        except Exception as e:
            print("输入有误！")
            continue
        if input_int < 1 or input_int > 100:
            print("范围有误！")
            continue
        return input_int


get_int()