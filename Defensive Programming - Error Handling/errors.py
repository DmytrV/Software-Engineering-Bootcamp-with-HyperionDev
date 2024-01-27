# Syntax Error: Missing parentheses for the print function
# Explanation: Print is a function and requires parentheses.
print("Welcome to the error program")

# Syntax Error 1: Missing parentheses for the print function
# Explanation: Print is a function and requires parentheses.
# Syntax Error 2: Incorrect space indentation
# Explanation: Needs to be in line with print function listed above
print("\n")

# Compilation Error: Incorrect space indentation
# Explanation: Next 5 lines of code should be in line with print function listed above

# Variables declaring the user's age, casting the str to an int, and printing the result
# Syntax Error 1: Using '==' instead of '=' for variable assignment
# Explanation: The correct syntax for variable assignment is '=', not '=='.
# Runtime Error 2: The input string '24 years old' cannot be directly converted to an integer
# Explanation: The string contains non-numeric characters, making it invalid for conversion to an integer.
age_Str = "24"
age = int(age_Str)

# Runtime Error 1: Trying to concatenate strings and integer without converting the integer to a string
# Explanation: We need to convert 'age' to a string before concatenating it with other strings.
# Logical Error 2: The absence or presence of a space in the output
# can lead to a logical error if the output doesn't match the expected result.
# Explanation: If we don't put space after "I'm" and before "years old"
# we'll receive output not what we expected for.
print("I'm " + str(age) + " years old.")

# Variables declaring additional years and printing the total years of age

# Logical Error 1: In line 65 we received output which doesn't meet with the result we expected,
# because in line 37 we put value which led to an issue at the end of the program.
# Explanation: Output "In 3 years and 6 months..." consists statement which doesn't meet with variable "total_months".
# Variable "total_months" consists presents years old which is 24 and additional years old which is 3 years.
# We lost 6 month, what should contain variable "years_from_now"
years_from_now = "3.5"
# Runtime Error: We can't make addition between float and string variables without converting the string to float
# Explanation: Python doesn't allow direct addition between float and string.
total_years = age + float(years_from_now)

# Syntax Error 1: Missing parentheses for the print function
# Explanation: Print is function and requires parentheses
# Syntax Error 2: Misspelling the variable.
# Explanation: Instead of variable "total_years" it was "answer_years".
# Logical Error 3: The absence or presence of a space in the output
# can lead to a logical error if the output doesn't match the expected result.
# Explanation: If we don't put space after "The total number of years:"
# we'll receive output not what we expected for.
# Logical Error 4: If put string instead of variable which consists some value,
# we'll receive output which doesn't match the expected result.
# Explanation: Instead of concatenate the string "The total number of years: " and variable str(total_years),
# we concatenated the string "The total number of years: " and the string "total_years" what lead to wrong output.
# Runtime Error 5: Trying to concatenate strings and float without converting the float to the string
# Explanation: We need to convert "total_years" to a string before concatenating it with other strings.
print("The total number of years: " + str(total_years))

# Variable to calculate the total amount of months from the total amount of years and printing the result
# Syntax Error: Misspelling the variable.
# Explanation: Instead of variable "total_years" we wrote total".
total_months = total_years * 12

# Syntax Error 1: Missing parentheses for the print function.
# Explanation: Print function in Python requires parentheses.
# Runtime Error 2: Trying to concatenate strings and float without converting the float to the string
# Explanation: We need to convert 'total_months' to a string before concatenating it with other strings.
# To get clear result without decimal we should first convert it to int then to string
print("In 3 years and 6 months, I'll be " + str(int(total_months)) + " months old")  # HINT, 330 months is
# the correct answer
