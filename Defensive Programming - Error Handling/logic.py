# Program to calculate the average of two numbers

# Input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Logical error: Incorrect calculation of the average
average = num1 + num2 / 2  # Logical error: Missing parentheses for correct order of operations

# Output
print("The average of", num1, "and", num2, "is:", average)
