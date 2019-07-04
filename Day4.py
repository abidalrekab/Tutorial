

# day 4 classes instantiations

class Employee:
    raise_amount = 1.04
    num_employee = 0

    def __init__(self,name,last_name, pay):
        self.name = name
        self.last_name = last_name
        self.pay = pay
        self.Email = name + last_name + '@' + 'gmail.com'
        Employee.num_employee += 1

    def get_info(self):
        return 'Name: {} \nLast Name: {} \nThe pay: {} \nThe Email: {}'.format(self.name, self.last_name, self.pay,
                                                                               self.Email)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def getting_raise(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        name1, last_name1, pay1 = emp_str.split('-')
        return cls(name1, last_name1, pay1)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, name, last_name, pay, prog_lange):
        super().__init__(name, last_name, pay)
        self.prog_lange = prog_lange


class Manager(Employee):

    raise_amount = 1.5

    def __init__(self, name, last_name, pay, employees=None):
        super().__init__(name, last_name, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print(emp.get_info())


dev_1 = Developer('Corey', 'Schafer', 50000, 'c++')
dev_2 = Developer('Terasa', 'Johonton', 43000, 'java')

mgr_1 = Manager('sue', 'woody', 90000, [dev_1])
mgr_1.print_emp()
mgr_1.add_employee(dev_2)
print(mgr_1.get_info())
mgr_1.print_emp()


