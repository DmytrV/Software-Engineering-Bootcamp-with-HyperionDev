"""
Create variable "name".
Assign "input" function to "name" variable.

Create variable "gender".
Assign empty string to "gender" variable.

Create variable "form_of_verb".
Assign empty string to "form_of_verb" variable.

Create variable "gender_neutral_title".
Assign the result of the “input” function to "gender_neutral_title" variable.
if "gender_neutral_title" equal Mx
    reassign variable "gender" to "They"
    reassign variable "form_of_verb" to "are"
else if "gender_neutral_title" equal Mr
    reassign variable "gender" to "He"
    reassign variable "form_of_verb" to "is"
else if "gender_neutral_title" equal Ms or Miss or Mrs
    reassign variable "gender" to "She"
    reassign variable "form_of_verb" to "is"

Create variable "age".
Assign the result of the “input” function to the “age” variable.

Create variable "number_of_house".
Assign the result of the "input" function to the "number_of_house" variable.

Create variable "street_name".
Assign the result of the "input" function to the "street_name" variable.

Output f-string through the function "print".

"""
name = input("Please enter your name so we know how to call you: ")
gender = ""
form_of_verb = ""
gender_neutral_title = input(f"{name}, please enter your gender-neutral title: Mx, Ms, Miss, Mrs or Mr. "
                             f"So that we can address you respectfully: ")
if gender_neutral_title == "Mx":
    gender = "They"
    form_of_verb = "are"
elif gender_neutral_title == "Mr":
    gender = "He"
    form_of_verb = "is"
elif gender_neutral_title == "Ms" or "Miss" or "Mrs":
    gender = "She"
    form_of_verb = "is"
age = input(f"{name}, please enter your age: ")
house_number = input(f"{name}, please enter your house number so we know where to send the post: ")
street_name = input(f"{name}, and last, enter your street name to be sure we send your correspondence to "
                    f"the correct address: ")
print(
    f"This is {name}. {gender} "
    f"{form_of_verb} {age} years old and "
    f"lives at house number {house_number} at {street_name}.")
