# Python Installation and Setup Guide

## Before the Workshop

### 1. Install Python

#### Windows:
1. Go to https://python.org/downloads/
2. Download Python 3.11 or later
3. Run the installer
4. **IMPORTANT**: Check "Add Python to PATH" during installation
5. Verify installation by opening Command Prompt and typing: `python --version`

#### macOS:
1. Go to https://python.org/downloads/
2. Download Python 3.11 or later
3. Run the installer
4. Verify installation by opening Terminal and typing: `python3 --version`

#### Linux (Ubuntu/Debian):
```bash
sudo apt update
sudo apt install python3 python3-pip
python3 --version
```

### 2. Install a Code Editor

#### Recommended: Visual Studio Code
1. Go to https://code.visualstudio.com/
2. Download and install
3. Install Python extension:
   - Open VS Code
   - Go to Extensions (Ctrl+Shift+X)
   - Search for "Python"
   - Install the official Python extension by Microsoft

#### Alternative Editors:
- PyCharm Community Edition
- Sublime Text
- Atom
- Even Notepad++ works!

### 3. Verify Everything Works

1. Create a new file called `test.py`
2. Add this code:
```python
print("Hello, Python!")
print("Python version:", __import__('sys').version)
```
3. Run the file:
   - In VS Code: Press F5 or use Run button
   - In terminal: `python test.py` (Windows) or `python3 test.py` (Mac/Linux)

## Workshop Day Setup

### Create Workshop Folder
```bash
# Create a folder for the workshop
mkdir python-workshop
cd python-workshop
```

### Download Workshop Files
You can download all the workshop files from this repository or create them as we go through the lessons.

## Python Basics Quick Reference

### Running Python Code

#### Interactive Mode (Python Shell):
```bash
python          # Windows
python3         # Mac/Linux
```

#### Running Python Files:
```bash
python filename.py          # Windows
python3 filename.py         # Mac/Linux
```

#### In VS Code:
- Press F5 to run current file
- Or right-click and select "Run Python File in Terminal"

### Getting Help

#### In Python shell:
```python
help(function_name)
dir(object_name)
type(variable_name)
```

#### Online Resources:
- Python.org documentation
- Stack Overflow
- Real Python tutorials

## Troubleshooting

### Common Issues:

#### "python is not recognized" (Windows)
- Python not added to PATH during installation
- Reinstall Python and check "Add Python to PATH"
- Or manually add Python to PATH in System Properties

#### "command not found: python" (Mac/Linux)
- Try `python3` instead of `python`
- Install Python using package manager

#### VS Code not recognizing Python
- Install Python extension
- Select Python interpreter: Ctrl+Shift+P → "Python: Select Interpreter"

#### Module import errors
- Make sure you're in the correct directory
- Check file names for typos
- Ensure Python can find your files

### Getting Unstuck During Workshop:

1. **Read the error message carefully** - it usually tells you what's wrong
2. **Check for typos** - variable names, function names, syntax
3. **Verify indentation** - Python is picky about spaces/tabs
4. **Ask for help** - don't struggle alone!
5. **Use print() statements** - to debug and see what's happening

## Workshop Structure

### Files We'll Create:
1. `01_hello_world.py` - First Python program
2. `02_variables_datatypes.py` - Variables and data types
3. `03_operations.py` - Basic operations
4. `04_control_flow.py` - If statements and loops
5. `05_data_structures.py` - Lists, dictionaries, tuples
6. `06_functions.py` - Creating and using functions
7. `07_file_handling.py` - Reading and writing files
8. `08_todo_app.py` - Final project

### Learning Approach:
- **Explanation** - Concept introduction
- **Demonstration** - Live coding examples
- **Practice** - Hands-on exercises
- **Q&A** - Questions and problem-solving

## After the Workshop

### Continue Learning:
1. **Practice daily** - Even 15 minutes helps
2. **Build projects** - Apply what you learned
3. **Join communities** - Python Discord, Reddit r/Python
4. **Read code** - Explore open-source projects
5. **Take online courses** - Coursera, edX, Udemy

### Project Ideas:
- Personal budget tracker
- Password generator
- Web scraper
- Simple games (guess the number, rock-paper-scissors)
- Automation scripts

### Next Steps:
- Learn web development (Flask/Django)
- Data science (pandas, matplotlib)
- Machine learning (scikit-learn)
- GUI applications (tkinter, PyQt)
- Game development (pygame)

Remember: Programming is learned by doing. The more you practice, the better you'll become!
