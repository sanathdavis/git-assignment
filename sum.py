# Program to calculate the sum of two numbers

# function to add two numbers
def add(num1, num2):
    return num1 + num2

# input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# call the function and store the result
result = add(num1, num2)

# print the result
print("The sum of", num1, "and", num2, "is:", result)
