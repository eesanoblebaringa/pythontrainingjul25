# PYTHON BEST PRACTICES - TIPS AND TRICKS...


# Full Stack Ascent 

#        (\__/)
#        (•ㅅ•)      Don’t talk to
#     ＿ノヽ ノ＼＿      me or my son
# `/　`/ ⌒Ｙ⌒ Ｙ  ヽ     ever again.
# ( 　(三ヽ人　 /　  |
# |　ﾉ⌒＼ ￣￣ヽ   ノ
# ヽ＿＿＿＞､＿_／
#       ｜( 王 ﾉ〈  (\__/)
#        /ﾐ`ー―彡\  (•ㅅ•)
#       / ╰    ╯ \ /    \>

# 1 - Why does it matter?
#    - Performance
#    - Security
#    - Readability
#        - Debugging
#        - Collaboration
#    - Maintainability
#      - Extensibility
#      - Refactoring

# 2 - PEP 8
#     - Naming Conventions
#     - Spacing around operators
#     - imports
#     - Blank lines
#     - Line length
#     - Linters and Formatters

# 3 - Readability Tips

# 3.1 - Descriptive Naming

# Variables, Functions, Classes names should be descriptive.
# e.g. calc_a() vs calculate_area()

# 3.2 - Comments and Docstrings

# Use comments to explain really complex sections of your code.
# Comments should be used sparingly and only when necessary. But don’t overdo it - your code should be self-explanatory.
# For functions and classes, write docstrings to describe what they do, their parameters, and return values.


def calculate_area(radius):
    # This function calculates the area of a circle.
    # The formula is: area = pi * radius^2
    # radius is the input to the function.
    # The radius represents the distance from the center of the circle to its edge.
    # The area is the total space enclosed by the circle.
    
    pi = 3.14159  # pi is a constant used in the area calculation
    # Using the formula for the area of a circle.
    area = pi * radius * radius  # multiplying pi by radius squared
    
    # The area has been calculated.
    return area  # returning the result of the area


def calculate_area(radius):
    """
    Calculate the area of a circle given its radius.
    
    Parameters:
    radius (float): The radius of the circle.
    
    Returns:
    float: The area of the circle.
    """
    
    pi = 3.14159
    area = pi * radius * radius
    
    return area


# 3.3 - Constants over Magic Numbers and Strings
# Magic numbers and strings are hard-coded values that are used in your code. Instead of using these, use constants.
# This makes your code more readable and maintainable. (if we need to change the value, we only need to change it in one place)

def calculate_area(radius):
    """
    Calculate the area of a circle given its radius.
    
    Parameters:
    radius (float): The radius of the circle.
    
    Returns:
    float: The area of the circle.
    """
    
    pi = 3.14159
    area = pi * radius * radius
    
    return area



from constants import PI

def calculate_area(radius):
    """
    Calculate the area of a circle given its radius.
    
    Parameters:
    radius (float): The radius of the circle.
    
    Returns:
    float: The area of the circle.
    """
    area = PI * radius * radius  # Area formula: pi * radius^2
    
    return area



# 3.3 - Avoid Deep Nesting
# This is ugly and I don't like it.

def process_data(data):
    if data:
        for item in data:
            if isinstance(item, dict):
                if 'name' in item:
                    if item['name'] == 'Alice':
                        print(f"Found Alice: {item}")
                    else:
                        print(f"Name is not Alice: {item}")
                else:
                    print("No 'name' key found in item")
            else:
                print("Item is not a dictionary")

#    There are lots of ways to refactor this code to make it more readable.
#    We will cover some of these in the next sections.

# 3.4 - SUPER FUN EXERCISE 1:

# Refactor the code below to make it more readable.

def v(items):
    r = []
    for i in items:
        if i['child']:
            r.append(i['price'] * 1.05)  # Children's items have 5% VAT. Because in this made up world that's how much VAT children's items have. And also because I said so.
        else:
            r.append(i['price'] * 1.2)  # Standard VAT is 20% for adults. An adult is defined as someone who is not a child. This is a very important distinction.
    return r

test_items = [
    {'price': 100, 'child': True},
    {'price': 200, 'child': False},
    {'price': 300, 'child': True},
    {'price': 400, 'child': False}
    ]

# UNCOMMENT THE LINE BELOW TO TEST YOUR FUNCTION
# print(v(test_items))

# 4 - Functions and Modularity

# 4.1 - Single Responsibility Principle
# Functions should do one thing and do it well.
# If a function is doing too much, consider breaking it down into smaller functions.
# e.g.:

def process_items(items):
    # Validate items
    for item in items:
        if 'price' not in item or 'is_child' not in item:
            raise ValueError("Each item must have 'price' and 'is_child' keys.")

    # Calculate VAT and update items
    for item in items:
        if item['is_child']:
            item['final_price'] = item['price'] * 1.05  # Reduced VAT
        else:
            item['final_price'] = item['price'] * 1.2  # Standard VAT

    # Print report
    print("Processed Items:")
    for item in items:
        print(f"Item: {item}, Final Price: {item['final_price']}")

    return items

# Improve readability by breaking it down into smaller functions:

def validate_order(order):
    """Validate the order data."""
    if not order.get('items'):
        raise ValueError("Order must have at least one item.")

def calculate_total(order):
    """Calculate the total price of the order."""
    return sum(item['price'] for item in order['items'])

def send_confirmation_email(email):
    """Send a confirmation email."""
    print(f"Sending confirmation email to {email}.")

def process_order(order):
    """Process the order by coordinating its steps."""
    validate_order(order)
    total = calculate_total(order)
    send_confirmation_email(order['email'])
    return total

# 4.2 - DRY (Don’t Repeat Yourself)
# If you find yourself writing the same code over and over again, consider refactoring it into a function.

def calculate_tax_for_item_a(price):
    return price * 0.1  # Tax rate for item A is 10%

def calculate_tax_for_item_b(price):
    return price * 0.15  # Tax rate for item B is 15%

def calculate_tax_for_item_c(price):
    return price * 0.2  # Tax rate for item C is 20%

def process_items(items):
    for item in items:
        if item['type'] == 'A':
            item['tax'] = calculate_tax_for_item_a(item['price'])
        elif item['type'] == 'B':
            item['tax'] = calculate_tax_for_item_b(item['price'])
        elif item['type'] == 'C':
            item['tax'] = calculate_tax_for_item_c(item['price'])
    
    return items

items = [
    {'type': 'A', 'price': 100},
    {'type': 'B', 'price': 200},
    {'type': 'C', 'price': 300}
]

processed_items = process_items(items)
# print(processed_items)

# Refactor the code to avoid repetition:
def calculate_tax(price, tax_rate):
    """Calculate tax based on the price and tax rate."""
    return price * tax_rate

def process_items(items):
    tax_rates = {'A': 0.1, 'B': 0.15, 'C': 0.2}  # Tax rates by item type
    
    for item in items:
        tax_rate = tax_rates.get(item['type'])
        if tax_rate is not None:
            item['tax'] = calculate_tax(item['price'], tax_rate)
    
    return items

items = [
    {'type': 'A', 'price': 100},
    {'type': 'B', 'price': 200},
    {'type': 'C', 'price': 300}
]

processed_items = process_items(items)
# print(processed_items)

# 4.3 - Modules
# Use modules to organize your code.
# Modules are files containing Python code.
# They help you organize your code into logical units.
# They also help you reuse code across different parts of your project.

from maths_operations import calculate_area_of_circle, calculate_area_of_rectangle

areas = [
    calculate_area_of_circle(5),
    calculate_area_of_rectangle(3, 4)
]

# 4.4 - SUPER FUN EXERCISE 2:
# Refactor the code below.
import hashlib

def register_user(username, email, password):
    """
    Register a new user by performing email validation, password validation,
    password hashing, and saving the user to the database.
    """
    # Validate email
    if '@' not in email:
        raise ValueError("Invalid email address")

    # Validate password
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters")

    # Hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Save the user to the database (simulated here by a print statement)
    print(f"User {username} created with email {email} and hashed password {hashed_password}")


#  5 - More Cool Stuff I couldn't categorise
#  5.1 - Type Hinting
#  Types are the classification of data in Python. They define the operations that can be performed on the data.
#  In Python, everything is an object, and every object has a type. e.g. int, float, str, list, dict, etc.
#  Python is a dynamically typed language, which means that the type of a variable is determined at runtime and can change during the execution of the program.
#  Dynamic typing allows for flexibility but can lead to errors if not used carefully.

def calculate_total_price(items):
    total = 0
    for item in items:
        price = item['price']  # Price can be a float or a string
        total += price
    return total

# Sample items, some prices are passed as strings
order = [
    {'name': 'Apple', 'price': 1.2},
    {'name': 'Banana', 'price': 2.5},  # String price
    {'name': 'Cherry', 'price': 3.0}
]

total_price = calculate_total_price(order)
# print(f"Total Price: {total_price}")

#  It is for this reason that Python introduced type hints. Type hints are a way to specify the expected types of function arguments and return values.
#  They are not enforced by Python itself, but they can be used by static type checkers to catch type errors before runtime and help with readability.

from typing import List, Dict

def calculate_total_price(items: List[Dict[str, float]]) -> float:
    """
    Calculate the total price of a list of items. Prices can be either float or string.

    Parameters:
    - items (List[Dict[str, Union[float, str]]]): A list of dictionaries where each dictionary
      contains:
        - 'price': The price of the item, which can be a float or a string.
    
    Returns:
    - float: The total price of all items in the list.
    """
    total = 0
    for item in items:
        price = item['price']
        total += price
    return total

# 5.1 - Control Flow
#    Remember where I talked about ugly nesting? Well, here are some ways to avoid it using some control flow tricks.
#    - Early Returns

def process_order(order: dict) -> float:
    if order['status'] == 'paid':
        if order['items']:
            if all(item['price'] > 0 for item in order['items']):
                total = 0
                for item in order['items']:
                    total += item['price']
                return total
            else:
                return None  # Invalid price in one or more items
        else:
            return None  # No items in order
    else:
        return None  # Order is not paid


def process_order(order: dict) -> float:
    if order['status'] != 'paid':
        return None  # Return None if the order is not paid
    
    if not order['items']:
        return None  # Return None if there are no items
    
    if any(item['price'] <= 0 for item in order['items']):
        return None  # Return None if any item has an invalid price
    
    total = sum(item['price'] for item in order['items'])
    return total

# 5.1.1 - SUPER FUN EXERCISE 3:
# Refactor the code below to use early returns and improve readability.
def check_user_access(user: dict) -> bool:
    if user['active']:
        if user['age'] >= 18:
            if user['role'] == 'admin' or user['role'] == 'moderator':
                if user['email_verified']:
                    return True
                else:
                    return False  # Email not verified
            else:
                return False  # Invalid role
        else:
            return False  # User is underage
    else:
        return False  # User is not active

# 5.1.2 - SUPER FUN EXERCISE 4:
# Refactor the code below to use early returns and improve readability. HINT: Use continue...
def process_numbers(numbers: list) -> int:
    total = 0
    for number in numbers:
        if number >= 0:
            if number % 2 == 0:
                if number < 100:
                    total += number
                else:
                    pass  # Skip numbers >= 100
            else:
                pass  # Skip odd numbers
        else:
            pass  # Skip negative numbers
    return total

# 6 - Enumerate
#    Enumerate is a built-in Python function that allows you to loop over an iterable and have an automatic counter.
def process_items(items: list):
    for i in range(len(items)):
        item = items[i]
        print(f"Item {i}: {item}")

# Sample usage
items = ["apple", "banana", "cherry"]
# process_items(items)

# Refactor the code to use enumerate:

def process_items(items: list):
    for i, item in enumerate(items):
        print(f"Item {i}: {item}")

# Sample usage
items = ["apple", "banana", "cherry"]
# process_items(items)


# 7 - Zip
#    Zip is a built-in Python function that allows you to combine multiple iterables into a single iterable.
def print_student_scores(names, scores):
    for i in range(len(names)):
        print(f"{names[i]} scored {scores[i]}")

# Sample data
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

# print_student_scores(names, scores)

# Refactor the code to use zip:

def print_student_scores(names, scores):
    for name, score in zip(names, scores):
        print(f"{name} scored {score}")

# Sample data
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

# print_student_scores(names, scores)

# 7.1 SUPER FUN EXERCISE 5:
# You are given two lists:

# A list of student names.
# A list of their corresponding grades.
# Write a function that takes both lists and pairs each student with their grade. 
# The function should return a list of tuples, where each tuple contains a student's name and their grade.

students = ["Alice", "Bob", "Charlie"]
grades = [85, 92, 78]

# 7.2 SUPER FUN EXERCISE 6:
# You are working on a data processing task where you are given two lists:

# A list of employees' names.
# A list of their corresponding salaries.
# However, the salary data comes with some adjustments, and you need to apply a bonus to the salary based on the employee's role. 
# You have a third list that contains the roles of the employees (e.g., "Manager", "Developer", "Intern"). Each role corresponds to a different bonus:

# "Manager": 20% bonus
# "Developer": 10% bonus
# "Intern": 5% bonus

# Oh and I would also like a ID for each employee. The ID should be a unique number starting from 1 and incrementing by 1 for each employee.

# Write a function that takes the three lists (names, salaries, and roles) and returns a list of tuples. 

# Each tuple should contain the employee ID, employee's name, their adjusted salary (original salary plus the role-based bonus).
# Example Output:
[(1, "Alice", 60000), (2, "Bob", 66000), (3, "Charlie", 49500)]

# And by the way if the names and salaries lists are of unequal length, ensure that the function only processes the length of the shortest list.

# Sample data
names = ["Alice", "Bob", "Charlie", "David"]
salaries = [50000, 60000, 45000, 55000, 990000]
roles = ["Manager", "Developer", "Intern", "Developer"]

# 8 - == vs is
# == is used to compare the values of two objects.
# 'is' is used to compare the identities of two objects. i.e. whether they are the same object in memory.

a = [1, 2, 3]
b = [1, 2, 3]

# print(a == b)  # True, because the contents of the lists are the same


a = [1, 2, 3]
b = a  # b is assigned the same reference as a

# print(a is b)  # True, because a and b point to the same object in memory

# You'll use it most often when comparing to None.
# In this case, is is used because None is a singleton in Python (there is only one instance of None in memory), so we compare the identity rather than the value.

x = None

# if x is None:
#     print("x is None")

# NOT

# if x == None:
#     print("x is None")

# 9 - List Comprehensions Questions

#    List comprehensions are a concise way to create lists in Python.
#    They are sometimes more readable and efficient way to create lists compared to traditional for loops.

# 9.1 Write a list comprehension that extracts all the words in a list of strings that start with the letter "a" and have more than 3 letters.

words = ["apple", "bat", "art", "apricot", "banana"]

# 9.2 You are given a list of dictionaries representing students.
# Each dictionary contains the student's name and grade.
# Write a list comprehension that returns the names of students who scored more than 80.

students = [{"name": "Alice", "grade": 85}, {"name": "Bob", "grade": 75}, {"name": "Charlie", "grade": 90}]


# 9.3 Given a 2D matrix, transpose it (swap rows with columns) using a List Comprehension.

# Input:

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Output:

[[1, 4, 7], [2, 5, 8], [3, 6, 9]]


# 10 Generators / Lazy Iteration
#        - Generators are a type of iterable, like lists or tuples.
#        - They allow you to iterate over a sequence of items without storing them in memory.
#        - Generators are created using functions and the yield statement.
#        - They are useful when you need to generate a large number of items but don't need to store them all at once.
#        - Generators are lazy, meaning they generate items on the fly as they are requested.

# Read all lines of a large file into memory
def read_lines(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()  # This loads all lines into memory
    return lines

# lines = read_lines('large_file.txt')
# for line in lines:
#     # Process each line
#     print(line.strip())



# Generator that reads file lines one by one, without loading the entire file into memory
def read_lines(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            yield line  # Yield each line one at a time

# lines = read_lines('large_file.txt')
# for line in lines:
#     # Process each line
#     print(line.strip())


# 10.1 - SUPER FUN EXERCISE 6:
# Write a function that uses a generator to generate the Fibonacci sequence up to a given number of terms.
# Input: 5
# Output: 0, 1, 1, 2, 3

def fibonacci(n):
    pass

# for num in fibonacci(5):
#     print(num)

# 11 - Efficient Programming & O-Notation

# Why it matters:

# Performance: Optimizing for speed and resource usage.
# Scalability: Handling large inputs or high traffic.

# 11.1 - Big O Notation
# Big O notation describes the time complexity of an algorithm (how runtime grows with input size).

# O(1): Constant time. Operations take the same time regardless of input size.
# O(n): Linear time. Time grows directly with input size.
# O(log n): Logarithmic time. Time grows slower than input size.
# O(n^2): Quadratic time. Time grows quickly with input size.

# Common Examples:

# O(1): Accessing an element in a list by index.
# O(n): Iterating through a list.
# O(n^2): Nested loops (e.g., comparing each element with every other element).

# Tips for efficiency:

# Avoid unnecessary loops.
# Use built-in Python functions (e.g., sorted()) that are optimized.
# Consider data structures: Lists are O(n) for search, dictionaries are O(1).

# There is so much more to say about this but so little time - If interested, check out the resources below.
# https://www.youtube.com/watch?v=BgLTDT03QtU&t=12s
# https://medium.com/@stefentaime_10958/understanding-big-o-notation-with-real-world-python-examples-a4ed435b8a56#:~:text=In%20simpler%20terms%2C%20Big%20O,(1)%20%E2%80%94%20Constant%20Time%20Complexity

