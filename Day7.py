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

    def fullname(self):                              # this is called regular method and it takes self as an argument
        return self.name + ' ' + self.last_name
 
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


print(Employee.num_employees)
emp_1 = Employee('mohamed', 'Abidalrekab', 40000)
emp_2 = Employee('Ali', 'Abidy', 34000)
emp_3 = Employee('Omaro', 'Abidalre', 34000)
print(Employee.num_employees)
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

# emp_1.__dict__ called namespace!!

print(emp_1.__dict__)
print(emp_2.__dict__)
print(Employee.__dict__)
# print(Employee.fullname(emp_2))

# print('The first Employee is {}, and his Email is {}'.format(emp_1.name + ' ' + emp_1.last_name, emp_1.email))

# print('The Second Employee is {}, and his Email is {}'.format(emp_2.name + ' ' + emp_2.last_name, emp_2.email))
