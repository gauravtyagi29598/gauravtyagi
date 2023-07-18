def perform_operation(choice):
    if choice == 1:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 + num2
    elif choice == 2:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 - num2
    elif choice == 3:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero")
            return
    elif choice == 4:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 * num2
    elif choice == 5:
        first = float(input("Enter the first number: "))
        second = float(input("Enter the second number: "))
        result = (first + second) / 2
    else:
        print("Invalid choice")
        return

    if result < 0:
        print("NEGATIVE")
    else:
        print("Result:", result)

# Ask the user to choose an option
print("Select an option:")
print("1. Addition")
print("2. Subtraction")
print("3. Division")
print("4. Multiplication")
print("5. Average")

choice = int(input("Enter your choice (1-5): "))

# Perform the chosen operation
perform_operation(choice)
