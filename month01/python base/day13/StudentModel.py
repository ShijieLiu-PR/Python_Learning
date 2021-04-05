
class StudentModel:
    """
        学生数据模型类
    """
    stu_count = 100

    def __init__(self, name, age, score=0):
        self.__id = StudentModel.stu_count
        StudentModel.stu_count += 1
        self.name = name
        self.age = age
        self.score = score

    @property
    def idd(self):
        return self.__id

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

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

