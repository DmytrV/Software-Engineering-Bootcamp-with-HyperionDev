"""
Create variable "name".
Assign the result of function "input" to "name" variable.
Output the name of the user through the function "print".

Create variable "age".
Assign result of function "input" to "age" variable.
Output f-string "'Name' is 'age' years old" through the function "print"

Output string "Hello World"
"""
name = input("Enter your name: ")
print(name)

age = input(f"How old are you, {name}: ")
print(f"{name} is {age} years old")
print("Hello World")
