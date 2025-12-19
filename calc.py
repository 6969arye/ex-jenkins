def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("אי אפשר לחלק באפס")
    return a / b


def substract(a, b):
    return a - b