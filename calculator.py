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
operations={"+": add, "-": subtract, "*": multiply, "**": power, "%": modulo, "/": divide}     
while True:
        while True:
            try:
                a = float(input("Enter first number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        while True:
            try:
                b = float(input("Enter second number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        while True:  
            op = input("Enter operator (+, -, *,**,%, /): ")
            try:
                print("Result:", operations[op](a,b))
                break
            except KeyError:
                print("Invalid operator. Please try again.")
        again = input("Do you want to perform another calculation? (y/n): ")
        if again == "n":
            break