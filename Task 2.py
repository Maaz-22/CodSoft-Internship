# Task 2

# For addition
def add(x, y):
    return x + y

# for subtraction
def subtract(x, y):
    return x - y

# For division
def divide(x, y):
    try:
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return x / y
    except ZeroDivisionError as i:
        return str(i)


# For multiplication
def multiply(x, y):
    return x * y

print ("Welcoe to the Calculator")
while True:

    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'divide' for division")
    print("Enter 'multiply' for multiplication")
    print("Enter 'quit' for the program to end ")

    userinput = input(": ")

    if userinput == "quit":
        print("Thankyou")
        break
    elif userinput in ("add", "subtract", "divide", "multiply"):
        num1 = float(input("Enter the  first number: "))
        num2 = float(input("Enter the second number: "))

        if userinput == "add":
            print("The Result is :", add(num1, num2))
        elif userinput == "subtract":
            print("The Result is :", subtract(num1, num2))
        elif userinput == "multiply":
            print("The Result is :", multiply(num1, num2))
        elif userinput == "divide":
            result = divide(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print("The Result is :", result)
        else:
            print("The input is invalid")
    else:
        print("The input is Invalid ")