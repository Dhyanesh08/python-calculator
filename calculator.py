print("simple calculator")

a = float(input("Enter first number: "))
op = input("Enter operator (+, -, *,%, /): ")
b = float(input("Enter second number: "))

if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "%":
    print("Result:", a % b)
elif op == "/":
    print("Result:", a / b)
    if b == 0:
        print("Cannot divide by zero")
    else:
        print("Result:", a / b)
else:
    print("Invalid operator")