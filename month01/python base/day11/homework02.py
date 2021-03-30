"""
2. 一家公司，有如下几种岗位：
    普通员工：底薪
    程序员：底薪 + 项目分红
    销售员：底薪 + 销售额
    定义员工管理器类，记录所有员工，提供计算总薪资的方法。
    要求：增加新岗位，员工管理器代码不做修改。
"""


class Staff:
    def __init__(self, name, base_pay):
        self.name = name
        self.base_pay = base_pay

    def get_salary(self):
        return self.base_pay


class Programer(Staff):
    def __init__(self, name, base_pay, bonus):
        super().__init__(name, base_pay)
        self.bonus = bonus

    def get_salary(self):
        return self.base_pay + self.bonus


class Sale(Staff):
    def __init__(self, name, base_pay, count):
        super().__init__(name, base_pay)
        self.count = count

    def get_salary(self):
        return self.base_pay + self.count


class Manager:
    def __init__(self):
        self.staff_list = list()

    def add_staff(self, staff):
        self.staff_list.append(staff)

    def get_total_pay(self):
        sum = 0
        for item in self.staff_list:
            sum += item.get_salary()
        return sum


s1 = Staff("zhangsan", 20000)
p1 = Programer("lisi", 50000, 30000)
sl1 = Sale("wangwu", 10000, 50000)
print(s1.get_salary())
print(p1.get_salary())
print(sl1.get_salary())
m1 = Manager()
m1.add_staff(s1)
m1.add_staff(p1)
m1.add_staff(sl1)
print(m1.get_total_pay())