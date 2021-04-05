"""
    ui 表示层
"""
from bll import *
from model import *
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

