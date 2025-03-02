#Task: Create a program that:
#1. Asks the user for two numbers and an operation (+, -, *, /).
#2. Performs the operation and displays the result.

num1 = float(input("What is you first number? "))
op = input("Select: +,-,/,* ")
num2 = float(input("What is you second number? "))

match op:
    case "+":
        # Using f-string
        print(f"The answer is: {num1 + num2}")
        # Using .format()
        #print("The answer is: {}".format(num1 * num2))
        # Using % operator
        #print("The answer is: %d" % (num1 * num2))
        # Using concatenation (need to convert to string)
        #print("The answer is: " + str(num1 * num2))
    case "-":
        print(f"The answer is: {num1 - num2}")
    case "/":
        print(f"The answer is: {num1 / num2}")
    case "*":
        # Using f-string
        print(f"The answer is: {num1 * num2}")
    case _:
        print(f"Improper Operator Used")


###
###
###

while True:
    try:
        num1 = float(input("What is your first number? "))
        op = input("Select: +,-,/,* ")
        num2 = float(input("What is your second number? "))

        match op:
            case "+":
                print(f"The answer is: {num1 + num2}")
            case "-":
                print(f"The answer is: {num1 - num2}")
            case "/":
                if num2 == 0: raise ZeroDivisionError("Cannot divide by zero")
                print(f"The answer is: {num1 / num2}")
            case "*":
                print(f"The answer is: {num1 * num2}")
            case _:
                print(f"Error: Invalid operator '{op}'")

        if input("Calculate again? (y/n): ").lower() != 'y':
            break

    except ValueError:
        print("Error: Please enter valid numbers")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")