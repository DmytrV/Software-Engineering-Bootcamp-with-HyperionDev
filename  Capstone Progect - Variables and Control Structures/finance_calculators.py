import math

# Display the menu to users
print("Menu:")
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")

# Get the user's choice with input validation
while True:
    user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()
    if user_choice in ["investment", "bond"]:
        break
    else:
        print("Invalid choice. Please enter either 'investment' or 'bond'.")

# Code for investment calculation.
if user_choice == "investment":
    principal_amount = float(input("Enter the principal amount: "))
    while True:
        try:
            interest_rate = float(input("Enter the interest rate (put JUST NUMBER without '%'): ")) / 100
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    while True:
        try:
            number_year = int(input("Enter the number of years you plan on investing: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    while True:
        interest = input("Enter which type of interest you would like - simple or compound: ").lower()
        if interest in ["simple", "compound"]:
            break
        else:
            print("Invalid input. Please enter either 'simple' or 'compound'.")

    # Calculate the interest using formula for simple interest.
    if interest == "simple":
        total_amount = principal_amount * (1 + interest_rate * number_year)
        print(f"The interest earned on your investment will be: {total_amount:.2f}")

    # Calculate the interest using formula for compound interest.
    elif interest == "compound":
        total_amount = principal_amount * math.pow(1 + interest_rate, number_year)
        print(f"The interest earned on your investment will be: {total_amount:.2f}")

# Code for bond calculation.
elif user_choice == "bond":
    present_value = float(input("Enter the present value of the house: "))
    while True:
        try:
            interest_rate = float(input("Enter the interest rate (put JUST NUMBER without '%'):")) / 100 / 12
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    while True:
        try:
            number_month = int(input("Enter number of months to repay: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Calculate the monthly bond repayment using the formula for bond repayment.
    amount_repay = (interest_rate * present_value) / (1 - (1 + interest_rate) ** (-number_month))
    print(f"The monthly bond repayment will be: {amount_repay:.2f}")
