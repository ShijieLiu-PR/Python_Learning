class EmployeeManager:
    def __init__(self):
        self.__all_employee = list()

    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.__all_employee.append(employee)

    def get_total_salary(self):
        """
            comapute total salary
        :return:
        """
        total_salary = 0
        for item in self.__all_employee:
            total_salary += item.compute_salary()
        return total_salary

class Employee:
    """
        Employee class
        function:代表具体员工，隔离员工管理器与具体员工的变化。
    """
    def __init__(self, name, salary):
        self.name = name
        self.base_salary = salary

    def compute_salary(self):
        return self.base_salary


class Programmer(Employee):
    """
        Programmer class
    """
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def compute_salary(self):
        # return self.base_salary + self.bonus
        return super().compute_salary() + self.bonus



class Salesman(Employee):
    """
        Salesman class
    """
    def __init__(self, name, salary, sale_value):
        super().__init__(name, salary)
        self.sale_value = sale_value

    def compute_salary(self):
        # return self.base_salary + self.bonus
        return super().compute_salary() + self.sale_value




manager = EmployeeManager()
manager.add_employee(Employee("zhangsan",50000))
manager.add_employee(Programmer("lisi",60000, 10000))
manager.add_employee(Salesman("wangwu",30000,100000))

print(manager.get_total_salary())