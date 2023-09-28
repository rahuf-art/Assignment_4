# Function to square a number
def square_number(x):
    return x ** 2

# Input a list of integers from the user
input_str = input("Enter a list of integers separated by spaces: ")
input_list = [int(num) for num in input_str.split()]

# Use map to square all numbers in the list
result_list = list(map(square_number, input_list))

# Display the result
print("User List:", input_list)
print("Square List:", result_list)

