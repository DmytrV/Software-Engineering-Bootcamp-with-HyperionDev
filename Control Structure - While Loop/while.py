# Initialize variables
total_amount = 0
amount_of_numbers = 0
average_of_numbers = 0

# Get user numbers
while True:
    user_number = int(input("Please, enter a number (-1 to exit): "))

    # Check if the user wants to exit
    if user_number == -1:
        # Avoid division by zero if no valid numbers were entered
        if amount_of_numbers == 0:
            print("No valid numbers entered.")
        else:
            average_of_numbers = total_amount / amount_of_numbers
            print(f"The average of the entered numbers is: {average_of_numbers}")
        break

    # Update calculation for non-exit case
    total_amount += user_number
    amount_of_numbers += 1
