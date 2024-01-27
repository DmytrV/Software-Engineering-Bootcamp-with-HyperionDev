# Syntax Error: assignment error.
# Explanation: in this case, we want to assign the variable "animal" value "Lion",
# because it's string type it should be with quotation mark.
animal = "Lion"
animal_type = "cub"
number_of_teeth = 16

# Logical Error: We received output which we didn't expect.
# Explanation: When we want to use variables inside string we can use f-string,
# the f-string allows you to embed expressions inside string literals.
full_spec = f"This is a {animal}. It is a {number_of_teeth} and it has {animal_type} teeth"

# Syntax Error: Missing parentheses for the print function.
# Explanation: Print is function and requires parentheses.
print(full_spec)
