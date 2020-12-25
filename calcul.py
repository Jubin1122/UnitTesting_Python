def add(x, y):
    "Addition"
    return x+y

def subtract(x, y):
    "Subtraction"
    return x-y

def multiply(x, y):
    "Multiplication" 
    return x*y

def divide(x, y):
    "Divition"
    if y == 0:
        raise ValueError('Denominator cannot be zero!')
    return x/y

    