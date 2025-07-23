# 3.4 - SUPER FUN EXCERCISE 1:
# Refactor the code below to make it more readable.

def v(items):
    r = []
    for i in items:
        if i['child']:
            r.append(i['price'] * 0.05)  # Children's items have 5% VAT. Because in this made up world that's how much VAT children's items have. And also because I said so.
        else:
            r.append(i['price'] * 0.2)  # Standard VAT is 20% for adults. An adult is defined as someone who is not a child. This is a very important distinction.
    return r

test_items = [
    {'price': 100, 'child': True},
    {'price': 200, 'child': False},
    {'price': 300, 'child': True},
    {'price': 400, 'child': False}
    ]

print(v(test_items))

# ANS

from constants import REDUCED_VAT_RATE, STANDARD_VAT_RATE

def calculate_vat(items):
    """
    Calculate the VAT for a list of items.

    Parameters:
    items (list of dict): A list of dictionaries, each containing:
                          - 'price' (float): The base price of the item.
                          - 'child' (bool): Whether the item is for children.
                          
    Returns:
    list of float: A list of prices after applying the appropriate VAT rate.
    """
    vat_list = []
    for item in items:
        if item['child']:
            vat_list.append(item['price'] * REDUCED_VAT_RATE)  # Apply reduced VAT for children
        else:
            vat_list.append(item['price'] * STANDARD_VAT_RATE)  # Apply standard VAT for others
    return vat_list

test_items = [
    {'price': 100, 'child': True},
    {'price': 200, 'child': False},
    {'price': 300, 'child': True},
    {'price': 400, 'child': False}
    ]

# UNCOMMENT THE LINE BELOW TO TEST YOUR FUNCTION
print(calculate_vat(test_items))

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

# ANS

import hashlib

def validate_email(email):
    """
    Validate the format of the email.
    """
    if '@' not in email:
        raise ValueError("Invalid email address")

def validate_password(password):
    """
    Validate the strength of the password.
    """
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters")

def hash_password(password):
    """
    Hash the password using SHA-256.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def save_user_to_db(username, email, hashed_password):
    """
    Simulate saving the user to the database.
    """
    print(f"User {username} created with email {email} and hashed password {hashed_password}")

def register_user(username, email, password):
    """
    Register a new user by using separate functions for each step:
    - Validate email
    - Validate password
    - Hash the password
    - Save the user to the database
    """
    validate_email(email)
    validate_password(password)
    hashed_password = hash_password(password)
    save_user_to_db(username, email, hashed_password)

register_user("Alice", "alice@blah.com", "password123")


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
    

# ANS

def check_user_access(user: dict) -> bool:
    if not user['active']:
        return False

    if user['age'] < 18:
        return False

    if user['role'] not in ['admin', 'moderator']:
        return False

    if not user['email_verified']:
        return False

    return True


# 5.1.2 - SUPER FUN EXERCISE 4:
# Refactor the code below to use early returns and improve readability.
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

# ANS
def process_numbers(numbers: list) -> int:
    total = 0
    for number in numbers:
        if number < 0:
            continue

        if number % 2 != 0:
            continue

        if number >= 100:
            continue

        total += number

    return