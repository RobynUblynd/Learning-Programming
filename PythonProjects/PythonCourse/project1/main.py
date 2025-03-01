#Initial Project part 1
print('Initial Project part 1')
print('Hello, World!')

#Initial Project part 2
print('Initial Project part 2')
name = input('What is your name? ')
print(f'Hello, {name}!')

#Initial Project Extras
print('Initial Project Extras')
name = input('What is your name? ')
age = input('What is your age? ')
print(f"Hello, {name}! You are {age} years old.")

#Initial Project Extras (Error Correction)
print('Initial Project Extras (Error Correction)')
try:
    # Ensure the name is not empty
    while True:
        name = input('What is your name? ')
        if name.strip():  # Checks if name is non-empty after removing whitespace
            break
        else:
            print("Please enter a name.")

    # Ensure the age is a positive number
    while True:
        age_str = input('What is your age? ')
        try:
            age = float(age_str)  # Convert to float to allow decimals; use int() for integers only
            if age > 0:  # Ensure age is positive
                break
            else:
                print("Age must be a positive number.")
        except ValueError:
            print("That's not a valid age. Please enter a number.")

    # Print the greeting
    print(f"Hello, {name}! You are {age} years old.")
except (KeyboardInterrupt, EOFError):
    print("\nProgram interrupted by user.")