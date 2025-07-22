# Data Structures - Organizing and Storing Data

# ===============================
# LISTS
# ===============================

# Creating lists
fruits = ["apple", "banana", "orange", "grape"]
numbers = [1, 2, 3, 4, 5]
mixed_list = ["hello", 42, True, 3.14]
empty_list = []

print("Fruits:", fruits)
print("Numbers:", numbers)
print("Mixed list:", mixed_list)

# Accessing list elements (indexing starts at 0)
print("\nFirst fruit:", fruits[0])
print("Last fruit:", fruits[-1])  # Negative indexing
print("Second and third fruits:", fruits[1:3])  # Slicing

# List methods
fruits.append("kiwi")  # Add to end
print("After append:", fruits)

fruits.insert(1, "mango")  # Insert at specific position
print("After insert:", fruits)

removed_fruit = fruits.pop()  # Remove and return last item
print("Removed:", removed_fruit)
print("After pop:", fruits)

fruits.remove("banana")  # Remove specific item
print("After remove:", fruits)

# List operations
numbers = [1, 2, 3]
more_numbers = [4, 5, 6]
combined = numbers + more_numbers  # Concatenation
print("Combined lists:", combined)

repeated = numbers * 3  # Repetition
print("Repeated list:", repeated)

# List properties
print("Length of fruits:", len(fruits))
print("Is 'apple' in fruits?", "apple" in fruits)
print("Count of 'apple':", fruits.count("apple"))

# ===============================
# DICTIONARIES
# ===============================

# Creating dictionaries (key-value pairs)
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8
}

print("\nStudent dictionary:", student)

# Accessing dictionary values
print("Student name:", student["name"])
print("Student age:", student.get("age"))  # Safer way
print("Student year:", student.get("year", "Not specified"))  # Default value

# Adding and modifying dictionary items
student["year"] = "Junior"  # Add new key-value pair
student["gpa"] = 3.9       # Modify existing value
print("Updated student:", student)

# Dictionary methods
print("All keys:", list(student.keys()))
print("All values:", list(student.values()))
print("All items:", list(student.items()))

# Looping through dictionaries
print("\nStudent information:")
for key, value in student.items():
    print(f"{key}: {value}")

# Dictionary of lists
gradebook = {
    "Alice": [95, 87, 92, 88],
    "Bob": [78, 85, 82, 90],
    "Charlie": [92, 94, 89, 95]
}

print("\nGradebook:", gradebook)
print("Alice's grades:", gradebook["Alice"])

# ===============================
# TUPLES
# ===============================

# Creating tuples (immutable sequences)
coordinates = (10, 20)
colors = ("red", "green", "blue")
single_item_tuple = (42,)  # Note the comma!

print("\nCoordinates:", coordinates)
print("Colors:", colors)

# Accessing tuple elements
print("X coordinate:", coordinates[0])
print("Y coordinate:", coordinates[1])

# Tuple unpacking
x, y = coordinates
print(f"X: {x}, Y: {y}")

# Multiple assignment using tuples
name, age, city = ("Alice", 25, "New York")
print(f"Name: {name}, Age: {age}, City: {city}")

# Tuples are immutable (cannot be changed)
# coordinates[0] = 15  # This would cause an error!

# ===============================
# WORKING WITH NESTED STRUCTURES
# ===============================

# List of dictionaries
students = [
    {"name": "Alice", "age": 20, "major": "CS"},
    {"name": "Bob", "age": 19, "major": "Math"},
    {"name": "Charlie", "age": 21, "major": "Physics"}
]

print("\nAll students:")
for student in students:
    print(f"{student['name']} is {student['age']} years old, majoring in {student['major']}")

# Dictionary of lists
inventory = {
    "fruits": ["apple", "banana", "orange"],
    "vegetables": ["carrot", "broccoli", "spinach"],
    "dairy": ["milk", "cheese", "yogurt"]
}

print("\nInventory:")
for category, items in inventory.items():
    print(f"{category.title()}: {', '.join(items)}")

# ===============================
# LIST COMPREHENSIONS (Bonus!)
# ===============================

# Creating lists with list comprehensions
squares = [x**2 for x in range(1, 6)]
print("\nSquares:", squares)

even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print("Even numbers:", even_numbers)

# ===============================
# EXERCISES
# ===============================

# Exercise 1: Shopping list manager
# Create a shopping list (list)
# Add functions to:
# - Add items to the list
# - Remove items from the list
# - Display the current list
# - Check if an item is in the list

# Exercise 2: Student grade tracker
# Create a dictionary where keys are student names and values are lists of grades
# Add functions to:
# - Add a new student
# - Add a grade for a student
# - Calculate average grade for a student
# - Find the student with the highest average

# Exercise 3: Contact book
# Create a list of dictionaries, each representing a contact
# Each contact should have: name, phone, email
# Add functions to:
# - Add a new contact
# - Search for a contact by name
# - Display all contacts
# - Update a contact's information

# Exercise 4: Word frequency counter
# Given a sentence (string), create a dictionary that counts how many times each word appears
# Example: "hello world hello" → {"hello": 2, "world": 1}

# Exercise 5: Coordinate distance calculator
# Given a list of coordinate tuples [(x1, y1), (x2, y2), ...]
# Calculate the distance from the origin (0, 0) to each point
# Distance formula: sqrt(x² + y²)
# Return a list of distances
