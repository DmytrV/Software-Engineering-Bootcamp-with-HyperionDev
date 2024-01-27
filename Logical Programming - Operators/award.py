# This programme will help determine awards for persons participating in triathlon competitions.

# First, we'll get the results of swimming, running and cycling.
# swimming = int(input("Enter result in swimming: "))
# cycling = int(input("Enter result in cycling: "))
# running = int(input("Enter result in running: "))

# Then, we'll count the results and determine the awards that person receives.
# if swimming + cycling + running <= 100:
#     print("You receive an award of Provincial Colours.")
# elif 100 < swimming + cycling + running <= 105:
#     print("You receive an award of Provincial Half Colours.")
# elif 105 < swimming + cycling + running <= 110:
#     print("You receive an award of Provincial Scroll.")
# else:
#     print("You don't receive any award")

# Our current topic is Logical Operators. This solution more related with it.
# First, we'll get the results of swimming, running and cycling.
swimming = int(input("Enter result in swimming: "))
cycling = int(input("Enter result in cycling: "))
running = int(input("Enter result in running: "))

# Then, we'll count the results and determine the awards that person receives.
if swimming + cycling + running <= 100:
    print("You receive an award of Provincial Colours.")
elif swimming + cycling + running > 100 and swimming + cycling + running <= 105:
    print("You receive an award of Provincial Half Colours.")
elif swimming + cycling + running > 105 and swimming + cycling + running <= 110:
    print("You receive an award of Provincial Scroll.")
else:
    print("You don't receive any award")