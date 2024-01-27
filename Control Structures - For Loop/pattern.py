# First solution
# rows = 10 # Number of rows
# counter = 0  # To count rows in each pattern

# for i in range(0, rows):
#     if i < 5: # Check if the current row is in the first half of the pattern
#         counter += 1
#         print("*" * counter)
#
#     elif i > 5: # Check if the current row is in the second half of the pattern
#         counter -= 1
#         print("*" * counter)

# Second solution (more simple, more readable)
rows = 5  # Number of rows in the pattern

# Loop to iterate over each row
for i in range(2 * rows):
    # Check if the current row is in the first half of the pattern
    if i < rows:
        # Print '*' repeated 'i' times
        print('*' * i)
    else:
        # Print '*' repeated '(2 * n - i)' times for the second half
        print('*' * (2 * rows - i))
