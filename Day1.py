

# Day1 Classes intro
class empolee:
    def __init__(self, name, last, pay):
        self.name = name
        self.last = last
        self.email = name + '.' + last + '@gmail.com'
        self.pay = pay
        
    def print_inf(self):
        return 'The first name:  {} \nThe last name: {} \nThe pay: {} $ \nEmail: {}'.format(self.name, self.last, self.pay, self.email)


empolee1 = empolee('mohamed', 'abidalrekab',50000)
print(empolee1.print_inf())