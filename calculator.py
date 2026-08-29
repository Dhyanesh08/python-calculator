import math
print("simple calculator")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def power(a, b):
    return a ** b

def modulo(a, b):
    return a % b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def sqrt(a):
    if a < 0:
        return "Cannot take square root of negative number"
    return a ** (1/2)

def cbrt(a):
    if a < 0:
        return "Cannot take cube root of negative number"
    return a ** (1/3)

def sin(a):
    return math.sin(math.radians(a))

def cos(a):
    return math.cos(math.radians(a))

def log(a):
    if a <= 0:
        return "Cannot take logarithm of non-positive number"
    return math.log(a)

def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")

operations = {"+": add, "-": subtract, "*": multiply, "**": power, "%": modulo, "/": divide}
single_operations = {"sqrt": sqrt,"cbrt": cbrt, "sin": sin, "cos": cos, "log": log}
while True:
    while True:
        op = input("Enter operator (+, -, *, **, %, /, sqrt , cbrt, sin, cos, log): ")
        if op in single_operations:
            break
        else:
            print("Invalid operator. Please try again.")

    a = get_number("Enter first number: ")
    if op in single_operations:
        print("Result:", single_operations[op](a))
    else:
        b = get_number("Enter second number: ")
        print("Result:", operations[op](a, b))

    again = input("Do you want to perform another calculation? (y/n): ")
    if again == "n":
        break