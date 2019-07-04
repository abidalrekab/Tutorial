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
        print(self.raise_amount)
        print(self.pay)
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, empl_str):
        name, last_name, pay = empl_str.split('-')
        pay = float(pay)
        return cls(name, last_name, pay)


# let's create an object from a class Employee using a string parsing in the form Name-last_name-pay
employee1 = 'Ali-Abidalrekab-33000'
employee2 = 'Hoda-Ashtar-33499'
employee3 = 'Absy-lokomoly-33040'
print(Employee.num_employees)
emp_1 = Employee.from_string(employee1)
emp_2 = Employee.from_string(employee2)
emp_3 = Employee.from_string(employee3)
emp_3.raise_amount = 1.04
emp_3.set_raise_amt(1.3)
emp_3.apply_raise()
print(emp_3.pay)
# this is the old technique to create an object
print(Employee.num_employees)
emp_4 = Employee('mohamed', 'Abidalrekab', 40000)
emp_5 = Employee('Ali', 'Abidy', 34000)
emp_6 = Employee('Omaro', 'Abidalre', 34000)
print(Employee.num_employees)
print(emp_4.pay)
emp_4.apply_raise()
print(emp_4.pay)

# emp_1.__dict__ called namespace!!

print(emp_1.__dict__)
print(emp_4.__dict__)
print(Employee.__dict__)
# print(Employee.fullname(emp_2))

# print('The first Employee is {}, and his Email is {}'.format(emp_1.name + ' ' + emp_1.last_name, emp_1.email))

# print('The Second Employee is {}, and his Email is {}'.format(emp_2.name + ' ' + emp_2.last_name, emp_2.email))
