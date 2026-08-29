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
    return a ** 0.5

operations = {"+": add, "-": subtract, "*": multiply, "**": power, "%": modulo, "/": divide}

while True:
    while True:
        op = input("Enter operator (+, -, *, **, %, /, sqrt): ")
        if op == "sqrt" or op in operations:
            break
        else:
            print("Invalid operator. Please try again.")

    while True:
        try:
            a = float(input("Enter first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    if op == "sqrt":
        print("Result:", sqrt(a))
    else:
        while True:
            try:
                b = float(input("Enter second number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        print("Result:", operations[op](a, b))

    again = input("Do you want to perform another calculation? (y/n): ")
    if again == "n":
        break