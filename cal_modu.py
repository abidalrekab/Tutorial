# today we explore the test module in python


def add(x, y):
    """ add function """
    return x + y


def subtract(x, y):
    """subtracting func"""
    return x - y

def multiplication(x, y):
    """ applying multiplication"""
    return x * y


def division(x, y):
    """return division """
    if y == 0 :
        raise ValueError('No division by zeros is allowed')

    return x/y



