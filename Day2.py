

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

e1 = Employee('Mohamed', 'Abidalrekab', 30300)
e2 = Employee('ALi', 'Abidalrekab', 120000)
e3 = Employee('Omar', 'Abidalrekab', 210020)
Employee.apply_raise(1.08)
print(Employee.raise_amount)
print(e1.raise_amount)
print(e2.raise_amount)
print(e3.raise_amount)

