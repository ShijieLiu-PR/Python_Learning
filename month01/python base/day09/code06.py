"""
    使用属性封装变量
"""
class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age
    # def get_name(self):
    #     return self.name
    # def get_age(self):
    #     return self.age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

w01 = Wife("Lucy", 23)
w01.name = "Lily"
print(w01.age)
print(w01._Wife__age)