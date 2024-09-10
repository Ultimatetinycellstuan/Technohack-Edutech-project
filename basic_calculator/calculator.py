import math
##Calculator functions
def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers"""
    if y == "0":
      return 0
    return x / y

def sqrt(x):
    """Calculate the square root of a number"""
    return math.sqrt(x)
def exponent(x, y):
    return x ** y
while True:
    print("Basic Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Exponent")
    print("7. Quit")
    choice = input("Enter your choice (1-7): ")
##Choices
    if choice == "1":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", add(num1, num2))
    elif choice == "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", subtract(num1, num2))
    elif choice == "3":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", multiply(num1, num2))
    elif choice == "4":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", divide(num1, num2))
    elif choice == "5":
        num = float(input("Enter a number: "))
        print("Result:", sqrt(num))
    elif choice == "6":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", exponent(num1, num2))
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
