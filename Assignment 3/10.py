# Accept the sequence of comma-separated numbers from the console
numbers_input = input("Enter a sequence of comma-separated numbers: ")

# Split the input into individual numbers
numbers_list = numbers_input.split(",")

# Create a list and a tuple containing each number as a string
numbers_list_str = [str(num) for num in numbers_list]
numbers_tuple_str = tuple(numbers_list_str)

# Print the list and the tuple
print(numbers_list_str)
print(numbers_tuple_str)
