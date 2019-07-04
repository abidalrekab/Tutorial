# classes, instantiation
# a class variable ?
# instance variable!


class Employee:
    '''This class is to create an employee class which stores name
    , Last name, and pay. returns full name, apply raise.
    '''

    raise_amount = 1.04
    num_employees = 0

    def __init__(self, name, last_name, pay):
        self.name = name
        self.last_name = last_name
        self.pay = pay
        self.email = self.name + '_' + self.last_name + '@' + 'Hotmail.com'
        Employee.num_employees += 1

    def fullname(self):  # this is called regular method and it takes self as an argument
        return self.name + ' ' + self.last_name

    def apply_raise(self):

        # print(self.raise_amount)
        # print(self.pay)
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, empl_str):
        name, last_name, pay = empl_str.split('-')
        pay = float(pay)
        return cls(name, last_name, pay)

# inheritance from other classes


class Developer(Employee):

    def __init__(self, name, last_name, pay, prog_lang):
        super().__init__(name, last_name, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, name, last_name, pay, employees = None):
        super().__init__(name, last_name, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emply):
        if emply not in self.employees:
            self.employees.append(emply)

    def remove_emp(self,emply):
        if emply in self.employees:
            self.employees.remove(emply)

    def print_emply(self):
        for emp in self.employees:
            print(emp.fullname())



dev_1 = Developer('Ahamed','Mojahad',34500,'C++')
dev_2 = Developer('Ali','MOha',45000,'Python')
dev_2.apply_raise()
print(dev_2.prog_lang)
mgr1 = Manager('Mohamed','Possaifey',90000, [dev_1, dev_2])
mgr1.print_emply()