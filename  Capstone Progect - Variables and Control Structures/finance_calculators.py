import math

# Display the menu to users
print("Menu:")
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")

# Get the user's choice
user_choice = (input("Enter either 'investment' or 'bond' from the menu above to proceed: ")).lower()

# Code for investment calculation.
if user_choice == "investment":
    principal_amount = float(input("Enter the principal amount: "))
    interest_rate = float(input("Enter the interest rate (put JUST NUMBER without '%'): ")) / 100
    number_year = int(input("Enter the number of years you plan on investing: "))
    interest = (input("Enter which type of interest you would like - simple or compound: ")).lower()

    # Calculate the interest using formula for simple interest.
    if interest == "simple":
        total_amount = principal_amount * (1 + interest_rate * number_year)
        print(f"The interest earned on your investment will be: {total_amount:.2f}")
        # Not nice to see a lot of number after the decimal point/
        # and I found '.2f' formatting specifier that is used
        # to format the output of a floating-point number.

    # Calculate the interest using formula for compound interest.
    elif interest == "compound":
        total_amount = principal_amount * math.pow(1 + interest_rate, number_year)
        print(f"The interest earned on your investment will be: {total_amount:.2f}")

# Code for bond calculation.
elif user_choice == "bond":
    present_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the interest rate (put JUST NUMBER without '%'):")) / 100 / 12
    number_month = int(input("Enter number of month to repay: "))

    # Calculate the monthly bond repayment using the formula for bond repayment.
    amount_repay = (interest_rate * present_value) / (1 - (1 + interest_rate) ** (-number_month))
    print(f"The monthly bond repayment will be: {amount_repay:.2f}")

else:
    print("Invalid choice. Please enter either 'investment' or 'bond': ")
