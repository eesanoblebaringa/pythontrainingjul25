# Python Cheat Sheet - Quick Reference

## Basic Syntax

### Comments
```python
# This is a single-line comment

"""
This is a 
multi-line comment
"""
```

### Variables
```python
name = "Alice"          # String
age = 25                # Integer
height = 5.6            # Float
is_student = True       # Boolean
```

### Print Output
```python
print("Hello, World!")
print("Name:", name)
print(f"I am {age} years old")  # f-string
```

### Get Input
```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
```

## Data Types

### Numbers
```python
x = 10          # Integer
y = 3.14        # Float
z = 2 + 3j      # Complex
```

### Strings
```python
text = "Hello"
text = 'Hello'  # Both work
multi = """Multiple
lines"""

# String operations
text.upper()        # "HELLO"
text.lower()        # "hello"
len(text)          # 5
text + " World"    # "Hello World"
text * 3           # "HelloHelloHello"
```

### Booleans
```python
is_true = True
is_false = False
```

## Operators

### Arithmetic
```python
+    # Addition
-    # Subtraction
*    # Multiplication
/    # Division
//   # Floor division
%    # Modulus (remainder)
**   # Exponentiation
```

### Comparison
```python
==   # Equal to
!=   # Not equal to
<    # Less than
>    # Greater than
<=   # Less than or equal
>=   # Greater than or equal
```

### Logical
```python
and  # Both must be True
or   # At least one must be True
not  # Opposite
```

## Control Flow

### If Statements
```python
if condition:
    # code block
elif another_condition:
    # code block
else:
    # code block
```

### For Loops
```python
# Loop through range
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

# Loop through list
fruits = ["apple", "banana"]
for fruit in fruits:
    print(fruit)

# Loop with index
for i, fruit in enumerate(fruits):
    print(i, fruit)
```

### While Loops
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

### Loop Control
```python
break     # Exit loop
continue  # Skip to next iteration
```

## Data Structures

### Lists (Mutable)
```python
# Create
numbers = [1, 2, 3, 4]
mixed = [1, "hello", True]

# Access
first = numbers[0]      # 1
last = numbers[-1]      # 4
slice = numbers[1:3]    # [2, 3]

# Modify
numbers.append(5)       # Add to end
numbers.insert(0, 0)    # Insert at position
numbers.remove(2)       # Remove specific value
popped = numbers.pop()  # Remove and return last

# Check
len(numbers)            # Length
2 in numbers           # True if 2 is in list
numbers.count(1)       # Count occurrences
```

### Dictionaries (Key-Value Pairs)
```python
# Create
person = {"name": "Alice", "age": 25}

# Access
name = person["name"]           # "Alice"
age = person.get("age", 0)     # Safe access

# Modify
person["city"] = "New York"     # Add new key
person["age"] = 26              # Update existing

# Loop
for key in person:              # Loop through keys
    print(key, person[key])

for key, value in person.items():  # Loop through key-value pairs
    print(key, value)
```

### Tuples (Immutable)
```python
# Create
point = (10, 20)
colors = ("red", "green", "blue")

# Access
x = point[0]    # 10
y = point[1]    # 20

# Unpack
x, y = point
```

## Functions

### Define Functions
```python
def greet():
    print("Hello!")

def greet_person(name):
    print(f"Hello, {name}!")

def add(a, b):
    return a + b

def greet_with_default(name, greeting="Hello"):
    return f"{greeting}, {name}!"
```

### Call Functions
```python
greet()                    # No parameters
greet_person("Alice")      # One parameter
result = add(5, 3)         # Save return value
greet_with_default("Bob")  # Use default parameter
```

## File Handling

### Write to File
```python
# Write mode (overwrites existing file)
with open("file.txt", "w") as file:
    file.write("Hello, World!")

# Append mode (adds to existing file)
with open("file.txt", "a") as file:
    file.write("\nNew line")
```

### Read from File
```python
# Read entire file
with open("file.txt", "r") as file:
    content = file.read()

# Read line by line
with open("file.txt", "r") as file:
    for line in file:
        print(line.strip())

# Read all lines into list
with open("file.txt", "r") as file:
    lines = file.readlines()
```

## Error Handling

### Try-Except
```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(result)
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An error occurred: {e}")
```

## Common Built-in Functions

```python
len(object)           # Length of object
type(object)          # Type of object
str(object)           # Convert to string
int(object)           # Convert to integer
float(object)         # Convert to float
bool(object)          # Convert to boolean

range(start, stop, step)  # Generate range of numbers
enumerate(iterable)       # Get index and value
zip(iter1, iter2)        # Combine iterables

min(iterable)         # Minimum value
max(iterable)         # Maximum value
sum(iterable)         # Sum of values
sorted(iterable)      # Sorted copy

abs(number)           # Absolute value
round(number, digits) # Round number
```

## String Formatting

### f-strings (Recommended)
```python
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old")
print(f"Next year I'll be {age + 1}")
```

### .format() method
```python
print("My name is {} and I am {} years old".format(name, age))
print("My name is {0} and I am {1} years old".format(name, age))
```

## List Comprehensions

### Basic Syntax
```python
# [expression for item in iterable if condition]

# Create list of squares
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# Filter even numbers
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# Transform strings
words = ["hello", "world"]
caps = [word.upper() for word in words]  # ["HELLO", "WORLD"]
```

## Common Patterns

### Check if list is empty
```python
if not my_list:
    print("List is empty")
```

### Swap variables
```python
a, b = b, a
```

### Multiple assignment
```python
x, y, z = 1, 2, 3
```

### Check multiple conditions
```python
if value in [1, 2, 3, 4, 5]:
    print("Value is in range")
```

### Default dictionary value
```python
count = my_dict.get(key, 0)  # Returns 0 if key doesn't exist
```

Remember: Practice makes perfect! Use this cheat sheet as a quick reference while coding.
