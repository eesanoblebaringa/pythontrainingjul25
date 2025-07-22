# Functions - Reusable Code Blocks

# ===============================
# BASIC FUNCTIONS
# ===============================

# Function with no parameters
def greet():
    print("Hello, World!")

# Call the function
greet()

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")

# Function with multiple parameters
def add_numbers(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

add_numbers(5, 3)
add_numbers(10, 7)

# ===============================
# RETURN VALUES
# ===============================

# Function that returns a value
def multiply(x, y):
    return x * y

# Use the returned value
result = multiply(4, 6)
print("4 * 6 =", result)

# Function with multiple return values
def get_name_age():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    return name, age

# Unpack the returned tuple
user_name, user_age = get_name_age()
print(f"Hello {user_name}, you are {user_age} years old!")

# ===============================
# DEFAULT PARAMETERS
# ===============================

def greet_with_title(name, title="Mr./Ms."):
    print(f"Hello, {title} {name}!")

greet_with_title("Smith")  # Uses default title
greet_with_title("Johnson", "Dr.")  # Uses provided title

def power(base, exponent=2):
    return base ** exponent

print("5 squared:", power(5))      # Uses default exponent
print("2 cubed:", power(2, 3))     # Uses provided exponent

# ===============================
# KEYWORD ARGUMENTS
# ===============================

def create_profile(name, age, city="Unknown", occupation="Student"):
    profile = f"Name: {name}, Age: {age}, City: {city}, Job: {occupation}"
    return profile

# Different ways to call the function
print(create_profile("Alice", 25))
print(create_profile("Bob", 30, "New York"))
print(create_profile("Charlie", 28, occupation="Engineer"))
print(create_profile(age=22, name="Diana", city="Boston"))

# ===============================
# FUNCTIONS WITH LISTS AND DICTIONARIES
# ===============================

def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

grades = [85, 92, 78, 96, 88]
avg = calculate_average(grades)
print(f"Average grade: {avg:.2f}")

def find_max_value(data_dict):
    if not data_dict:
        return None
    return max(data_dict.values())

scores = {"Alice": 95, "Bob": 87, "Charlie": 92}
highest_score = find_max_value(scores)
print("Highest score:", highest_score)

# ===============================
# VARIABLE SCOPE
# ===============================

# Global variable
global_counter = 0

def increment_counter():
    global global_counter  # Access global variable
    global_counter += 1
    print(f"Counter: {global_counter}")

def local_example():
    local_var = "I'm local!"
    print(local_var)

increment_counter()
increment_counter()
local_example()
# print(local_var)  # This would cause an error!

# ===============================
# LAMBDA FUNCTIONS (Anonymous Functions)
# ===============================

# Regular function
def square(x):
    return x ** 2

# Lambda equivalent
square_lambda = lambda x: x ** 2

print("Square of 5:", square(5))
print("Square of 5 (lambda):", square_lambda(5))

# Lambda with multiple parameters
add = lambda x, y: x + y
print("3 + 4 =", add(3, 4))

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared_numbers)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

# ===============================
# PRACTICAL EXAMPLES
# ===============================

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def temperature_converter():
    """Interactive temperature converter."""
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = input("Choose conversion (1 or 2): ")
    temp = float(input("Enter temperature: "))
    
    if choice == "1":
        result = celsius_to_fahrenheit(temp)
        print(f"{temp}°C = {result:.2f}°F")
    elif choice == "2":
        result = fahrenheit_to_celsius(temp)
        print(f"{temp}°F = {result:.2f}°C")
    else:
        print("Invalid choice!")

# temperature_converter()  # Uncomment to run

def validate_email(email):
    """Simple email validation."""
    return "@" in email and "." in email.split("@")[-1]

def get_user_info():
    """Get and validate user information."""
    while True:
        name = input("Enter your name: ").strip()
        if name:
            break
        print("Name cannot be empty!")
    
    while True:
        email = input("Enter your email: ").strip()
        if validate_email(email):
            break
        print("Please enter a valid email!")
    
    while True:
        try:
            age = int(input("Enter your age: "))
            if age > 0:
                break
            print("Age must be positive!")
        except ValueError:
            print("Please enter a valid number!")
    
    return {"name": name, "email": email, "age": age}

# user_info = get_user_info()  # Uncomment to run
# print("User info:", user_info)

# ===============================
# EXERCISES
# ===============================

# Exercise 1: Calculator functions
# Create functions for: add, subtract, multiply, divide
# Each should take two parameters and return the result
# Create a main calculator function that asks user for operation and numbers

# Exercise 2: List utilities
# Create functions:
# - find_maximum(numbers): returns the largest number in a list
# - find_minimum(numbers): returns the smallest number in a list
# - remove_duplicates(items): returns a list with no duplicates
# - reverse_list(items): returns the list in reverse order

# Exercise 3: Password generator
# Create a function that generates a random password
# Parameters: length, include_uppercase, include_numbers, include_symbols
# Return a randomly generated password meeting the criteria

# Exercise 4: Grade calculator
# Create functions:
# - letter_grade(percentage): converts number grade to letter grade
# - calculate_gpa(grades): calculates GPA from list of letter grades
# - grade_statistics(grades): returns min, max, average, and median

# Exercise 5: Text analyzer
# Create functions:
# - word_count(text): counts words in text
# - character_count(text, include_spaces=True): counts characters
# - most_common_word(text): finds the most frequently used word
# - reverse_words(text): reverses the order of words in the text
