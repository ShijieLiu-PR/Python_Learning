"""
    数据模型类：StudentModel
        数据：编号id，姓名name，年龄age，成绩score
    逻辑控制类：StudentManagerController
        数据：学生列表__stu_list
        行为：获取列表stu_list，添加学生add_student,删除学生delete_student，修改学生update_student，根据成绩排序order_by_score.
    界面视图类：StudentManagerView
        数据：逻辑控制对象__manager
        行为：显示菜单__display_menu,选择菜单__select_menu,
"""
import random


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


class StudentManagerView:
    """
        界面视图类
    """

    def __init__(self):
        self.__stu_mager = StudentManagerController()

    def __input_student(self, stu):
        # 1.在控制台中录入学生信息，存成学生对象
        # 2.调用逻辑控制器的add_student方法
        self.__stu_mager.add_student(stu)

    def __out_student(self):
        self.__stu_mager.display_student()

    def __display_menu(self):
        print("1) 添加学生")
        print("2) 显示学生")
        print("3) 删除学生")
        print("4) 修改学生")
        print("5) 按照成绩降序排列")

    def __select_menu(self):
        number = input("请输入选项：")
        if number == "1":
            name = input("请输入学生姓名：")
            age = int(input("请输入学生年龄："))
            score = int(input("请输入学生成绩："))
            self.__input_student(StudentModel(name, age, score))

        elif number == "2":
            self.__stu_mager.display_student()
        elif number == "3":
            name = input("请输入删除学生的姓名：")
            self.__stu_mager.delete_stu(name)

        elif number == "4":
            name = input("请输入学生姓名：")
            age = int(input("请输入学生年龄："))
            score = int(input("请输入学生成绩："))
            self.__stu_mager.update_student(name, age, score)

        elif number == "5":
            print("成绩由高到低排序为：")
            self.__stu_mager.order_by_score()
            self.__out_student()

    def main(self):
        """
            界面入口方法
        :return:
        """
        while True:
            self.__display_menu()
            self.__select_menu()


stu_manager = StudentManagerController()
view = StudentManagerView()
view.main()


