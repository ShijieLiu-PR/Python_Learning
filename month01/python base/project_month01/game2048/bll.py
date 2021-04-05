"""
    bll业务逻辑层
"""

class StudentManagerController:
    """
        学生逻辑控制类
    """

    def __init__(self):
        self.__stu_list = list()

    @property
    def stu_list(self):
        return self.__stu_list

    def add_student(self, stu):
        self.stu_list.append(stu)

    def display_student(self):
        for item in self.stu_list:
            print(item.idd, item.name, item.age, item.score)

    def delete_stu(self, name):
        for i in range(len(self.stu_list)):
            if self.stu_list[i].name == name:
                del self.stu_list[i]

    def update_student(self, name, age, score):
        for i in range(len(self.stu_list)):
            if self.stu_list[i].name == name:
                self.stu_list[i].age = age
                self.stu_list[i].score = score

    def order_by_score(self):
        for i in range(len(self.stu_list) - 1):
            for j in range(i + 1, len(self.stu_list)):
                if self.stu_list[i].score < self.stu_list[j].score:
                    self.stu_list[i], self.stu_list[j] = self.stu_list[j], self.stu_list[i]
