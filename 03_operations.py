# Basic Operations

# ===============================
# ARITHMETIC OPERATIONS
# ===============================

# Basic math operations
a = 10
b = 3

print("Addition:", a + b)        # 13
print("Subtraction:", a - b)     # 7
print("Multiplication:", a * b)  # 30
print("Division:", a / b)        # 3.333...
print("Floor Division:", a // b) # 3 (integer division)
print("Modulus (remainder):", a % b)  # 1
print("Exponentiation:", a ** b) # 1000 (10 to the power of 3)

# Order of operations (PEMDAS)
result = 2 + 3 * 4
print("2 + 3 * 4 =", result)  # 14 (not 20!)

result_with_parentheses = (2 + 3) * 4
print("(2 + 3) * 4 =", result_with_parentheses)  # 20

# ===============================
# STRING OPERATIONS
# ===============================

# String concatenation
greeting = "Hello"
name = "World"
message = greeting + " " + name + "!"
print(message)

# String repetition
laugh = "Ha" * 5
print(laugh)  # HaHaHaHaHa

# String formatting (f-strings - modern way)
age = 25
name = "Alice"
formatted_message = f"My name is {name} and I am {age} years old"
print(formatted_message)

# String formatting with expressions
price = 19.99
tax_rate = 0.08
total = price * (1 + tax_rate)
print(f"Price: ${price}, Total with tax: ${total:.2f}")

# ===============================
# COMPARISON OPERATIONS
# ===============================

x = 5
y = 10

print("x == y:", x == y)  # Equal to
print("x != y:", x != y)  # Not equal to
print("x < y:", x < y)    # Less than
print("x > y:", x > y)    # Greater than
print("x <= y:", x <= y)  # Less than or equal to
print("x >= y:", x >= y)  # Greater than or equal to

# String comparisons
word1 = "apple"
word2 = "banana"
print("apple < banana:", word1 < word2)  # Alphabetical comparison

# ===============================
# LOGICAL OPERATIONS
# ===============================

# Boolean operations
is_sunny = True
is_warm = False

print("AND:", is_sunny and is_warm)  # Both must be True
print("OR:", is_sunny or is_warm)    # At least one must be True
print("NOT sunny:", not is_sunny)    # Opposite

# Combining conditions
temperature = 75
is_weekend = True

good_beach_day = (temperature > 70) and is_weekend
print("Good beach day:", good_beach_day)

# ===============================
# ASSIGNMENT OPERATIONS
# ===============================

# Compound assignment operators
counter = 10
print("Initial counter:", counter)

counter += 5  # Same as: counter = counter + 5
print("After += 5:", counter)

counter -= 3  # Same as: counter = counter - 3
print("After -= 3:", counter)

counter *= 2  # Same as: counter = counter * 2
print("After *= 2:", counter)

counter /= 4  # Same as: counter = counter / 4
print("After /= 4:", counter)

# ===============================
# EXERCISES
# ===============================

# Exercise 1: Calculator
# Get two numbers from the user and perform all arithmetic operations
# Remember to convert string input to numbers!

# Exercise 2: Temperature converter
# Get temperature in Celsius from user
# Convert to Fahrenheit using formula: F = C * 9/5 + 32
# Print both temperatures with descriptive text

# Exercise 3: Circle calculator
# Get radius from user
# Calculate and print:
# - Area (π * r²) - use 3.14159 for π
# - Circumference (2 * π * r)

# Exercise 4: Age checker
# Get user's age
# Check if they are:
# - A minor (under 18)
# - Can vote (18 or older)
# - Can rent a car (25 or older)
# Print appropriate messages for each condition
