print("Welcome to the calculator!")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum = num1+num2
difference = num1-num2
product = num1*num2
quotient = num1/num2

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice (1/2/3/4/5): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"The sum of {num1} and {num2} is: {add(num1, num2)}")
        elif choice == '2':
            print(f"The difference of {num1} and {num2} is: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The product of {num1} and {num2} is: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"The quotient of {num1} and {num2} is: {divide(num1, num2)}")
    elif choice == '5':
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid input. Please enter a number between 1 and 5.")
