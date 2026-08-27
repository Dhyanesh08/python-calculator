print("simple calculator")
def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def power(a,b):
    return a ** b
def modulo(a,b):
    return a % b
def divide(a,b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
a = float(input("Enter first number: "))
op = input("Enter operator (+, -, *,**,%, /): ")
b = float(input("Enter second number: "))
operations={"+": add, "-": subtract, "*": multiply, "**": power, "%": modulo, "/": divide}
print("Result:", operations[op](a,b))


