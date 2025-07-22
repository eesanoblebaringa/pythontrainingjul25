# Variables and Data Types

# Variables are containers for storing data
# Python has several built-in data types

# ===============================
# NUMBERS
# ===============================

# Integers (whole numbers)
age = 25
temperature = -5
population = 1000000

print("Age:", age)
print("Temperature:", temperature)

# Floats (decimal numbers)
price = 19.99
pi = 3.14159
weight = 72.5

print("Price: $", price)
print("Pi:", pi)

# ===============================
# STRINGS
# ===============================

# Strings are text data
name = "Alice"
city = 'New York'  # Single or double quotes work
message = """This is a 
multi-line string"""

print("Name:", name)
print("City:", city)
print("Message:", message)

# String operations
first_name = "John"
last_name = "Smith"
full_name = first_name + " " + last_name  # String concatenation
print("Full name:", full_name)

# String methods
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Length:", len(name))

# ===============================
# BOOLEANS
# ===============================

# Booleans represent True or False
is_sunny = True
is_raining = False
is_weekend = True

print("Is sunny:", is_sunny)
print("Is raining:", is_raining)

# ===============================
# TYPE CHECKING AND CONVERSION
# ===============================

# Check the type of a variable
print("Type of age:", type(age))
print("Type of price:", type(price))
print("Type of name:", type(name))
print("Type of is_sunny:", type(is_sunny))

# Type conversion
age_str = "30"
age_int = int(age_str)  # Convert string to integer
print("Converted age:", age_int)

price_str = str(price)  # Convert float to string
print("Price as string:", price_str)

# Converting user input (always comes as string)
user_age = input("Enter your age: ")
user_age_int = int(user_age)
next_year_age = user_age_int + 1
print(f"Next year you will be {next_year_age}")

# ===============================
# EXERCISES
# ===============================

# Exercise 1: Create variables for your personal information
# - Your name (string)
# - Your age (integer)
# - Your height in meters (float)
# - Whether you like Python (boolean)
# Print all of them with descriptive labels

# Exercise 2: Calculate and print the following:
# - Your age in months (age * 12)
# - Your age in days (approximate: age * 365)
# - Your height in centimeters

# Exercise 3: Get user input for:
# - Their favorite number (convert to integer)
# - Their favorite color (keep as string)
# Print: "Your favorite number times 2 is [result] and your favorite color is [color]"
