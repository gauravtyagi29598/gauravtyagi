# Function to replace last element with another list
def replace_last_element(list1, list2):
    list1[-1:] = list2

# Sample input
input_list = [1, 3, 5, 7, 9, 10]
replacement_list = [2, 4, 6, 8]

# Call the function to replace the last element
replace_last_element(input_list, replacement_list)

# Print the updated list
print(input_list)
