def print_divisible_strings(n):
    if n % 3 == 0 and n % 5 == 0:
        print("Consultadd - Python Training")
    elif n % 3 == 0:
        print("Consultadd")
    elif n % 5 == 0:
        print("Python Training")

# Example usage:
number = int(input("Enter a number: "))
print_divisible_strings(number)
