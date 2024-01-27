# Open the DOB.txt file for reading
with open("DOB.txt", 'r') as file:
    # Read all lines from the file
    dob_data = file.readlines()
    # print(dob_data)

    # Initialize empty lists to store names and birthdates separately
    names = []
    birthdates = []

    # Iterate through each line in the file
    for line in dob_data:
        # Split each line into parts based on whitespace
        parts = line.split()
        # print(parts)

        # Join the name parts (excluding the last three) to form the full name
        name = ' '.join(parts[:-3])
        # print(name)

        # Join the last three parts to form the birthdate
        birthdate = ' '.join(parts[-3:])
        # print(birthdate)

        # Append the name and birthdate to their respective lists
        names.append(name)
        birthdates.append(birthdate)

    # Print the formatted names section
    print("Name")
    print('\n'.join(names))

    # Print the formatted birthdates section
    print("\nBirthdate")
    print('\n'.join(birthdates))
