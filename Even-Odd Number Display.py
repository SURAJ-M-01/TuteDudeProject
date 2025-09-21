# Task 1: Check if a Number is Even or Odd
# This program takes a number from user and checks if it's even or odd

# Step 1: Get input from the user
number = int(input("Enter an integer: "))

# Step 2: Check if the number is even or odd using if-else statement
if number % 2 == 0:
    # If remainder is 0 when divided by 2, it's even
    print(f"{number} is even")
else:
    # If remainder is not 0, it's odd
    print(f"{number} is odd")
