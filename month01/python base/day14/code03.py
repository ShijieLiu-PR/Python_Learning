"""
    自定义异常
"""


class AgeError(Exception):
    def __init__(self, msg, code, age):
        super().__init__(msg)
        self.code = code
        self.age = age


class Wife:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if 20 <= value <= 30:
            self.__age = value
        else:
            # print("我不要！")
            raise AgeError("年龄范围有误!", 10003, value)
            self.__age = 0


try:
    w01 = Wife(89)
except AgeError as e:
    print(e.args)
    print(e.code)
    print(e.age)
