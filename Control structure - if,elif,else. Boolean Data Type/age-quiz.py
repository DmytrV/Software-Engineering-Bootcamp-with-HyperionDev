age = int(input("Enter your current age, please: "))
if age < 13:
    print("You qualify for the kiddie discount.")
elif age == 21:
    print("Congrats on your 21st!")
elif age >= 40:
    print("You're over the hill.")
elif age >= 65:
    print("Enjoy your retirement!")
elif age > 100:
    print("Sorry you are dead!")
else:
    print("Age is but a number.")
