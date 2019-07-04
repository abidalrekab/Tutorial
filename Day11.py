# Python OOP Tutorial 6: Property Decorators - Getters, Setters, and Deleters

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
        Employee.num_employees += 1

    @property
    def fullname(self):  # this is called regular method and it takes self as an argument
        return self.name + ' ' + self.last_name

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @property
    def email(self):
        return self.name + '_' + self.last_name + '@' + 'Hotmail.com'

    @fullname.setter
    def fullname(self,name):
        name, last_name = name.split(' ')
        self.name = name
        self.last_name = last_name

    @fullname.deleter
    def fullname(self):
        self.name = '****'
        self.last_name = '****'

emp1 = Employee('Adm','smith', 45000)
del emp1.fullname
print(emp1.name)
print(emp1.last_name)
print(emp1.pay)
print(emp1.fullname)
