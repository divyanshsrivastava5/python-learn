def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("can't divide with 0")
    return a / b