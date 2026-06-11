# calculator.py — has a bug for testing
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # BUG: no check for division by zero
    return a / b

result = divide(10, 0)   # This will crash at runtime
print(result)
print("BYEE")
