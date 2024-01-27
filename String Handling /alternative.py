# Task 1: Making each alternate character in the string uppercase and lowercase
original_string_1 = "Hello World"
modified_string_1 = ""

# Iterate through each character in the original string
for i in range(len(original_string_1)):
    # If the index is even, convert the character to uppercase
    if i % 2 == 0:
        modified_string_1 += original_string_1[i].upper()
    # If the index is odd, convert the character to lowercase
    else:
        modified_string_1 += original_string_1[i].lower()

# Print the result
print(modified_string_1)


# Task 2: Making each alternate word in the string lowercase and uppercase
original_string_2 = "I am learning to code"
word_list_2 = original_string_2.split()
modified_word_list_2 = []

# Iterate through each word in the list
for i in range(len(word_list_2)):
    # If the index is even, convert the entire word to lowercase
    if i % 2 == 0:
        modified_word_list_2.append(word_list_2[i].lower())
    # If the index is odd, convert the entire word to uppercase
    else:
        modified_word_list_2.append(word_list_2[i].upper())

# Print the intermediate list
print(modified_word_list_2)

# Join the list into a string with spaces between words
final_string_2 = " ".join(modified_word_list_2)

# Print the final result
print(final_string_2)
