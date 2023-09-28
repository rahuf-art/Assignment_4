# Define a lambda function
sum = lambda x: x + 25

num = int(input("Enter a number: "))

# Use the lambda function to add 25 to the input number
result = sum(num)
print(f"{num} + 25 = {result}")
