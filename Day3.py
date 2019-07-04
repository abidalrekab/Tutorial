

# day 2 classes continue

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
        return 'Name: {} \nLast Name: {} \nThe pay: {} \nThe Email: {}'.format(self.name,self.last_name,self.pay,self.Email)

    def getting_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def apply_raise(cls,amount):
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

# e1 = Employee('Mohamed', 'Abidalrekab', 30300)
# e2 = Employee('ALi', 'Abidalrekab', 120000)
# e3 = Employee('Omar', 'Abidalrekab', 210020)


e1 = 'Mohamed-Abidalrekab-30000'
e2 = 'ALi-Abidalrekab-120000'
e3 = 'Omar-Abidalrekab-23000'
name, last_name, pay = e1.split('-')
employee1 = Employee.from_string(e2)
print(employee1.__dict__)

import datetime
mydate = datetime.date(1967, 7, 6)
print(Employee.is_workday(mydate))