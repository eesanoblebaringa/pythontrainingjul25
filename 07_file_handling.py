# File Handling - Reading and Writing Files

# ===============================
# WRITING TO FILES
# ===============================

# Writing text to a file
def create_sample_file():
    """Create a sample text file for demonstration."""
    with open("sample.txt", "w") as file:
        file.write("Hello, World!\n")
        file.write("This is a sample file.\n")
        file.write("We're learning Python file handling.\n")
    print("Created sample.txt")

# Writing multiple lines at once
def write_shopping_list():
    """Write a shopping list to a file."""
    shopping_items = [
        "Apples\n",
        "Bananas\n", 
        "Milk\n",
        "Bread\n",
        "Eggs\n"
    ]
    
    with open("shopping_list.txt", "w") as file:
        file.writelines(shopping_items)
    print("Created shopping_list.txt")

# Appending to an existing file
def add_to_shopping_list(item):
    """Add an item to the shopping list."""
    with open("shopping_list.txt", "a") as file:
        file.write(f"{item}\n")
    print(f"Added {item} to shopping list")

# ===============================
# READING FROM FILES
# ===============================

# Reading entire file at once
def read_entire_file(filename):
    """Read and display entire file content."""
    try:
        with open(filename, "r") as file:
            content = file.read()
            print(f"Content of {filename}:")
            print(content)
    except FileNotFoundError:
        print(f"File {filename} not found!")

# Reading file line by line
def read_file_lines(filename):
    """Read and display file content line by line."""
    try:
        with open(filename, "r") as file:
            print(f"Lines in {filename}:")
            for line_number, line in enumerate(file, 1):
                print(f"Line {line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"File {filename} not found!")

# Reading lines into a list
def get_file_lines(filename):
    """Return file content as a list of lines."""
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            # Remove newline characters
            return [line.strip() for line in lines]
    except FileNotFoundError:
        print(f"File {filename} not found!")
        return []

# ===============================
# WORKING WITH CSV-LIKE DATA
# ===============================

def create_student_records():
    """Create a file with student records."""
    students = [
        "Name,Age,Grade,Subject\n",
        "Alice,20,A,Math\n",
        "Bob,19,B,Science\n",
        "Charlie,21,A,English\n",
        "Diana,20,C,History\n"
    ]
    
    with open("students.txt", "w") as file:
        file.writelines(students)
    print("Created students.txt")

def read_student_records():
    """Read and parse student records."""
    try:
        with open("students.txt", "r") as file:
            lines = file.readlines()
            
            # First line is header
            header = lines[0].strip().split(",")
            print("Student Records:")
            print("-" * 40)
            
            # Process each student record
            for line in lines[1:]:
                data = line.strip().split(",")
                student = dict(zip(header, data))
                print(f"Name: {student['Name']}, Age: {student['Age']}, "
                      f"Grade: {student['Grade']}, Subject: {student['Subject']}")
    except FileNotFoundError:
        print("students.txt not found!")

# ===============================
# FILE OPERATIONS AND ERROR HANDLING
# ===============================

import os

def file_exists(filename):
    """Check if a file exists."""
    return os.path.exists(filename)

def get_file_size(filename):
    """Get file size in bytes."""
    if file_exists(filename):
        return os.path.getsize(filename)
    return 0

def delete_file(filename):
    """Safely delete a file."""
    try:
        if file_exists(filename):
            os.remove(filename)
            print(f"Deleted {filename}")
        else:
            print(f"{filename} does not exist")
    except PermissionError:
        print(f"Permission denied: Cannot delete {filename}")

def list_files_in_directory(directory="."):
    """List all files in a directory."""
    try:
        files = os.listdir(directory)
        print(f"Files in {directory}:")
        for file in files:
            if os.path.isfile(file):
                print(f"  - {file}")
    except PermissionError:
        print(f"Permission denied: Cannot access {directory}")

# ===============================
# PRACTICAL EXAMPLES
# ===============================

def simple_note_taking_app():
    """A simple note-taking application."""
    notes_file = "notes.txt"
    
    while True:
        print("\n--- Simple Notes App ---")
        print("1. Write a note")
        print("2. Read all notes")
        print("3. Clear all notes")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            note = input("Enter your note: ")
            timestamp = input("Enter date (or press Enter for 'Today'): ") or "Today"
            
            with open(notes_file, "a") as file:
                file.write(f"[{timestamp}] {note}\n")
            print("Note saved!")
            
        elif choice == "2":
            if file_exists(notes_file):
                with open(notes_file, "r") as file:
                    notes = file.read()
                    if notes:
                        print("\n--- Your Notes ---")
                        print(notes)
                    else:
                        print("No notes found.")
            else:
                print("No notes file found.")
                
        elif choice == "3":
            if file_exists(notes_file):
                delete_file(notes_file)
                print("All notes cleared!")
            else:
                print("No notes to clear.")
                
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

def word_frequency_analyzer(filename):
    """Analyze word frequency in a text file."""
    try:
        with open(filename, "r") as file:
            text = file.read().lower()
            
            # Remove punctuation and split into words
            import string
            translator = str.maketrans("", "", string.punctuation)
            clean_text = text.translate(translator)
            words = clean_text.split()
            
            # Count word frequencies
            word_count = {}
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1
            
            # Sort by frequency (most common first)
            sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
            
            print(f"\nWord frequency analysis for {filename}:")
            print("-" * 40)
            for word, count in sorted_words[:10]:  # Top 10 words
                print(f"{word}: {count}")
                
    except FileNotFoundError:
        print(f"File {filename} not found!")

# ===============================
# DEMONSTRATION
# ===============================

def demonstrate_file_operations():
    """Demonstrate various file operations."""
    print("File Handling Demonstration")
    print("=" * 30)
    
    # Create sample files
    create_sample_file()
    write_shopping_list()
    create_student_records()
    
    # Add item to shopping list
    add_to_shopping_list("Cheese")
    
    # Read files
    print("\n--- Reading Files ---")
    read_entire_file("sample.txt")
    print()
    read_file_lines("shopping_list.txt")
    print()
    read_student_records()
    
    # File information
    print("\n--- File Information ---")
    print(f"sample.txt exists: {file_exists('sample.txt')}")
    print(f"sample.txt size: {get_file_size('sample.txt')} bytes")
    
    # List current directory files
    print()
    list_files_in_directory()

# Run demonstration
if __name__ == "__main__":
    demonstrate_file_operations()

# ===============================
# EXERCISES
# ===============================

# Exercise 1: Personal diary
# Create a diary application that:
# - Asks for today's date and diary entry
# - Saves each entry to a file with date and content
# - Can display all previous entries
# - Can search for entries containing specific words

# Exercise 2: Contact manager
# Create a contact management system that:
# - Stores contacts in a text file (name, phone, email)
# - Can add new contacts
# - Can search for contacts by name
# - Can display all contacts
# - Can update existing contacts

# Exercise 3: Grade book manager
# Create a program that:
# - Reads student grades from a file
# - Calculates average grade for each student
# - Finds the highest and lowest grades
# - Saves a summary report to a new file

# Exercise 4: Log file analyzer
# Create a program that:
# - Reads a log file with timestamps and messages
# - Counts how many entries are from each day
# - Finds the most common error messages
# - Creates a summary report

# Exercise 5: Configuration file handler
# Create functions to:
# - Read configuration from a file (key=value format)
# - Update specific configuration values
# - Save configuration back to file
# - Validate configuration values
