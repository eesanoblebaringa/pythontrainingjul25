# Control Flow - Making Decisions and Repeating Actions

# ===============================
# IF STATEMENTS
# ===============================

# Basic if statement
age = 18

if age >= 18:
    print("You are an adult!")

# if-else statement
temperature = 75

if temperature > 80:
    print("It's hot outside!")
else:
    print("It's not too hot.")

# if-elif-else statement
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Multiple conditions
weather = "sunny"
temperature = 75

if weather == "sunny" and temperature > 70:
    print("Perfect day for a picnic!")
elif weather == "rainy" or temperature < 50:
    print("Better stay inside.")
else:
    print("Decent day to go out.")

# ===============================
# FOR LOOPS
# ===============================

# Loop through a range of numbers
print("Counting from 1 to 5:")
for i in range(1, 6):  # range(start, stop)
    print(i)

# Loop through a range with steps
print("\nEven numbers from 0 to 10:")
for i in range(0, 11, 2):  # range(start, stop, step)
    print(i)

# Loop through a string
name = "Python"
print(f"\nLetters in '{name}':")
for letter in name:
    print(letter)

# Loop through a list
fruits = ["apple", "banana", "orange", "grape"]
print("\nFruits in our list:")
for fruit in fruits:
    print(f"- {fruit}")

# Loop with index using enumerate
print("\nFruits with their position:")
for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")

# ===============================
# WHILE LOOPS
# ===============================

# Basic while loop
print("\nCountdown:")
count = 5
while count > 0:
    print(count)
    count -= 1  # Decrease count by 1
print("Blast off!")

# While loop with user input
print("\nGuessing game:")
secret_number = 7
guess = 0

while guess != secret_number:
    guess = int(input("Guess the number (1-10): "))
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Correct! You got it!")

# ===============================
# LOOP CONTROL STATEMENTS
# ===============================

# break - exit the loop early
print("\nFinding the first number divisible by 7:")
for i in range(1, 20):
    if i % 7 == 0:
        print(f"Found it: {i}")
        break
    print(f"Checking {i}...")

# continue - skip the current iteration
print("\nOdd numbers from 1 to 10:")
for i in range(1, 11):
    if i % 2 == 0:  # if even
        continue    # skip this iteration
    print(i)

# ===============================
# NESTED LOOPS
# ===============================

# Multiplication table
print("\nMultiplication table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        result = i * j
        print(f"{i} x {j} = {result}")
    print()  # Empty line after each row

# ===============================
# EXERCISES
# ===============================

# Exercise 1: Grade calculator
# Ask the user for 5 test scores
# Calculate the average
# Determine letter grade using if-elif-else
# Print the average and letter grade

# Exercise 2: Number guesser
# Computer picks a random number between 1-20
# User has 5 attempts to guess
# Give hints (too high/too low) after each wrong guess
# Congratulate if they win, reveal answer if they lose

# Exercise 3: Password validator
# Ask user to create a password
# Check if it meets criteria:
# - At least 8 characters long
# - Contains at least one uppercase letter
# - Contains at least one lowercase letter
# - Contains at least one number
# Keep asking until they create a valid password

# Exercise 4: Fibonacci sequence
# Print the first 10 numbers in the Fibonacci sequence
# (Each number is the sum of the two preceding ones: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34)

# Exercise 5: Pattern printer
# Print the following pattern:
# *
# **
# ***
# ****
# *****
