
# Special (Magic/Dunder) Methods

# any name surrounding by __ is called Dunder

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

    def __repr__(self):
        ''' This special method is used to check from which this instance is instantiated '''
        return "Employee('{}', '{}',{})".format(self.name, self.last_name, self.pay)

    def __str__(self):
        ''' This special function is to display instance information to the end-user '''
        return "{} - {}".format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay


# inheritance from other classes
emply1 = Employee('Nancy', 'Hood', 54500)
emply2 = Employee('Alies', 'Green', 90009)
print(emply1 + emply2)
