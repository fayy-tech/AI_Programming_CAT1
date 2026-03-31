# Ask the user to enter a number
number = int(input("Enter a number: "))

# Check if the number is negative
if number < 0:
    print("Invalid input – negative numbers not allowed.")

# Check if the number is even
elif number % 2 == 0:
    print("The number is even.")

# Otherwise the number is odd
else:
    print("The number is odd.")