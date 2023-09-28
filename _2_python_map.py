# Function to triple a number
def triple_number(x):
    return x * 3

# Input a list of integers from the user
input_str = input("Enter a list of integers separated by spaces: ")
input_list = [int(num) for num in input_str.split()]

# Use map to triple all numbers in the list
result_list = list(map(triple_number, input_list))

# Display the result
print("User List:", input_list)
print("Tripled List:", result_list)

