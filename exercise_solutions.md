# Exercise Solutions and Examples

This file contains solution examples for the exercises in each lesson.

## 01_hello_world.py Solutions

### Exercise 1: Age Program
```python
name = input("What's your name? ")
age = input("What's your age? ")
print(f"Nice to meet you, {name}! You are {age} years old!")
```

### Exercise 2: Greeting Program
```python
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
favorite_color = input("Enter your favorite color: ")
print(f"Hello {first_name} {last_name}! I see your favorite color is {favorite_color}.")
```

## 02_variables_datatypes.py Solutions

### Exercise 1: Personal Information
```python
my_name = "Alice"
my_age = 25
my_height = 1.65
likes_python = True

print(f"Name: {my_name}")
print(f"Age: {my_age}")
print(f"Height: {my_height} meters")
print(f"Likes Python: {likes_python}")
```

### Exercise 2: Age Calculations
```python
age = 25
age_in_months = age * 12
age_in_days = age * 365
height_in_meters = 1.65
height_in_cm = height_in_meters * 100

print(f"Age in months: {age_in_months}")
print(f"Age in days: {age_in_days}")
print(f"Height in centimeters: {height_in_cm}")
```

## 03_operations.py Solutions

### Exercise 1: Calculator
```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Addition: {num1} + {num2} = {num1 + num2}")
print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
print(f"Multiplication: {num1} * {num2} = {num1 * num2}")
print(f"Division: {num1} / {num2} = {num1 / num2}")
```

### Exercise 2: Temperature Converter
```python
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius * 9/5 + 32
print(f"{celsius}°C = {fahrenheit}°F")
```

## 04_control_flow.py Solutions

### Exercise 1: Grade Calculator
```python
total = 0
for i in range(5):
    score = float(input(f"Enter test score {i+1}: "))
    total += score

average = total / 5

if average >= 90:
    letter_grade = "A"
elif average >= 80:
    letter_grade = "B"
elif average >= 70:
    letter_grade = "C"
elif average >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"

print(f"Average: {average:.2f}")
print(f"Letter Grade: {letter_grade}")
```

### Exercise 4: Fibonacci Sequence
```python
a, b = 0, 1
print("First 10 Fibonacci numbers:")
for i in range(10):
    print(a, end=" ")
    a, b = b, a + b
print()
```

## 05_data_structures.py Solutions

### Exercise 1: Shopping List Manager
```python
shopping_list = []

def add_item():
    item = input("Enter item to add: ")
    shopping_list.append(item)
    print(f"Added {item} to the list")

def remove_item():
    item = input("Enter item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"Removed {item} from the list")
    else:
        print(f"{item} not found in the list")

def display_list():
    if shopping_list:
        print("Shopping List:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")
    else:
        print("Shopping list is empty")

def check_item():
    item = input("Enter item to check: ")
    if item in shopping_list:
        print(f"{item} is in the list")
    else:
        print(f"{item} is not in the list")
```

## 06_functions.py Solutions

### Exercise 1: Calculator Functions
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero!"

def calculator():
    while True:
        print("\n1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Quit")
        
        choice = input("Choose operation: ")
        
        if choice == "5":
            break
        
        if choice in ["1", "2", "3", "4"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == "1":
                result = add(num1, num2)
            elif choice == "2":
                result = subtract(num1, num2)
            elif choice == "3":
                result = multiply(num1, num2)
            elif choice == "4":
                result = divide(num1, num2)
            
            print(f"Result: {result}")
        else:
            print("Invalid choice!")
```

### Exercise 2: List Utilities
```python
def find_maximum(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def find_minimum(numbers):
    if not numbers:
        return None
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

def remove_duplicates(items):
    unique_items = []
    for item in items:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items

def reverse_list(items):
    return items[::-1]
```

## Workshop Tips and Best Practices

### Code Style
- Use descriptive variable names
- Add comments to explain complex logic
- Keep functions small and focused
- Use consistent indentation (4 spaces)

### Debugging Tips
1. Use print() statements to check variable values
2. Read error messages carefully
3. Check for typos in variable names
4. Ensure proper indentation
5. Use the Python debugger (pdb) for complex issues

### Common Beginner Mistakes
1. Forgetting to convert input() to int/float
2. Using = instead of == for comparison
3. Incorrect indentation
4. Not handling empty lists/strings
5. Off-by-one errors in loops

### Resources for Further Learning
- Python.org documentation
- Real Python tutorials
- Automate the Boring Stuff with Python
- Python Crash Course book
- Codecademy Python course
