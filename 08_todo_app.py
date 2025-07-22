#!/usr/bin/env python3
"""
Todo List Application - Final Project
=====================================

A command-line todo list application that demonstrates all the Python concepts
we've learned in this workshop:

- Variables and data types
- Control flow (if/else, loops)
- Data structures (lists, dictionaries)
- Functions
- File handling
- Error handling

Features:
- Add new tasks
- Mark tasks as complete
- View all tasks
- Delete tasks
- Save/load from file
- Priority levels
- Due dates
"""

import os
from datetime import datetime, date


class TodoApp:
    """A simple todo list application."""
    
    def __init__(self, filename="todos.txt"):
        """Initialize the todo app with a filename for persistence."""
        self.filename = filename
        self.todos = []
        self.load_todos()
    
    def load_todos(self):
        """Load todos from file if it exists."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    for line in file:
                        line = line.strip()
                        if line:
                            # Parse the line: status|priority|task|due_date
                            parts = line.split("|")
                            if len(parts) >= 3:
                                todo = {
                                    "task": parts[2],
                                    "completed": parts[0] == "True",
                                    "priority": parts[1] if len(parts) > 1 else "Medium",
                                    "due_date": parts[3] if len(parts) > 3 and parts[3] != "None" else None,
                                    "created": parts[4] if len(parts) > 4 else str(date.today())
                                }
                                self.todos.append(todo)
                print(f"Loaded {len(self.todos)} todos from {self.filename}")
            except Exception as e:
                print(f"Error loading todos: {e}")
    
    def save_todos(self):
        """Save todos to file."""
        try:
            with open(self.filename, "w") as file:
                for todo in self.todos:
                    line = f"{todo['completed']}|{todo['priority']}|{todo['task']}|{todo['due_date']}|{todo['created']}\n"
                    file.write(line)
            print("Todos saved successfully!")
        except Exception as e:
            print(f"Error saving todos: {e}")
    
    def add_todo(self):
        """Add a new todo item."""
        print("\n--- Add New Todo ---")
        task = input("Enter task description: ").strip()
        
        if not task:
            print("Task cannot be empty!")
            return
        
        # Get priority
        print("Priority levels: 1=High, 2=Medium, 3=Low")
        priority_choice = input("Enter priority (1-3, default=2): ").strip()
        priority_map = {"1": "High", "2": "Medium", "3": "Low"}
        priority = priority_map.get(priority_choice, "Medium")
        
        # Get due date (optional)
        due_date = input("Enter due date (YYYY-MM-DD, or press Enter to skip): ").strip()
        if due_date:
            try:
                # Validate date format
                datetime.strptime(due_date, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format! Using no due date.")
                due_date = None
        else:
            due_date = None
        
        # Create todo item
        todo = {
            "task": task,
            "completed": False,
            "priority": priority,
            "due_date": due_date,
            "created": str(date.today())
        }
        
        self.todos.append(todo)
        print(f"Added todo: '{task}' with priority {priority}")
    
    def view_todos(self):
        """Display all todos."""
        if not self.todos:
            print("\nNo todos found! Add some tasks to get started.")
            return
        
        print(f"\n--- Your Todos ({len(self.todos)} total) ---")
        print()
        
        # Group by completion status
        pending_todos = [todo for todo in self.todos if not todo["completed"]]
        completed_todos = [todo for todo in self.todos if todo["completed"]]
        
        # Display pending todos
        if pending_todos:
            print("📋 PENDING TASKS:")
            for i, todo in enumerate(pending_todos):
                self._display_todo(todo, i + 1)
        
        # Display completed todos
        if completed_todos:
            print("\n✅ COMPLETED TASKS:")
            for i, todo in enumerate(completed_todos):
                self._display_todo(todo, len(pending_todos) + i + 1)
    
    def _display_todo(self, todo, index):
        """Helper method to display a single todo."""
        status = "✅" if todo["completed"] else "⏳"
        priority_emoji = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}
        priority_indicator = priority_emoji.get(todo["priority"], "⚪")
        
        due_info = ""
        if todo["due_date"]:
            due_info = f" (Due: {todo['due_date']})"
        
        print(f"{index:2d}. {status} {priority_indicator} {todo['task']}{due_info}")
    
    def complete_todo(self):
        """Mark a todo as completed."""
        if not self.todos:
            print("No todos to complete!")
            return
        
        self.view_todos()
        try:
            choice = int(input("\nEnter todo number to mark as complete: "))
            if 1 <= choice <= len(self.todos):
                todo = self.todos[choice - 1]
                if todo["completed"]:
                    print("This todo is already completed!")
                else:
                    todo["completed"] = True
                    print(f"Marked '{todo['task']}' as completed! 🎉")
            else:
                print("Invalid todo number!")
        except ValueError:
            print("Please enter a valid number!")
    
    def delete_todo(self):
        """Delete a todo item."""
        if not self.todos:
            print("No todos to delete!")
            return
        
        self.view_todos()
        try:
            choice = int(input("\nEnter todo number to delete: "))
            if 1 <= choice <= len(self.todos):
                todo = self.todos.pop(choice - 1)
                print(f"Deleted '{todo['task']}'")
            else:
                print("Invalid todo number!")
        except ValueError:
            print("Please enter a valid number!")
    
    def search_todos(self):
        """Search for todos containing specific text."""
        if not self.todos:
            print("No todos to search!")
            return
        
        search_term = input("Enter search term: ").strip().lower()
        if not search_term:
            print("Search term cannot be empty!")
            return
        
        matching_todos = []
        for i, todo in enumerate(self.todos):
            if search_term in todo["task"].lower():
                matching_todos.append((i + 1, todo))
        
        if matching_todos:
            print(f"\nFound {len(matching_todos)} todos matching '{search_term}':")
            for index, todo in matching_todos:
                self._display_todo(todo, index)
        else:
            print(f"No todos found matching '{search_term}'")
    
    def show_statistics(self):
        """Show todo statistics."""
        if not self.todos:
            print("No todos to analyze!")
            return
        
        total = len(self.todos)
        completed = len([todo for todo in self.todos if todo["completed"]])
        pending = total - completed
        
        # Priority breakdown
        priority_count = {"High": 0, "Medium": 0, "Low": 0}
        for todo in self.todos:
            priority_count[todo.get("priority", "Medium")] += 1
        
        # Overdue tasks
        overdue = 0
        today = date.today()
        for todo in self.todos:
            if not todo["completed"] and todo["due_date"]:
                try:
                    due_date = datetime.strptime(todo["due_date"], "%Y-%m-%d").date()
                    if due_date < today:
                        overdue += 1
                except ValueError:
                    pass
        
        print("\n--- Todo Statistics ---")
        print(f"Total todos: {total}")
        print(f"Completed: {completed} ({completed/total*100:.1f}%)")
        print(f"Pending: {pending} ({pending/total*100:.1f}%)")
        print(f"Overdue: {overdue}")
        print("\nPriority breakdown:")
        for priority, count in priority_count.items():
            print(f"  {priority}: {count}")
    
    def display_menu(self):
        """Display the main menu."""
        print("\n" + "=" * 40)
        print("         📝 TODO LIST APP         ")
        print("=" * 40)
        print("1. 📋 View all todos")
        print("2. ➕ Add new todo")
        print("3. ✅ Mark todo as complete")
        print("4. 🗑️  Delete todo")
        print("5. 🔍 Search todos")
        print("6. 📊 Show statistics")
        print("7. 💾 Save and exit")
        print("8. 🚪 Exit without saving")
        print("=" * 40)
    
    def run(self):
        """Main application loop."""
        print("Welcome to the Todo List App!")
        print("Manage your tasks efficiently! 🎯")
        
        while True:
            self.display_menu()
            choice = input("Choose an option (1-8): ").strip()
            
            if choice == "1":
                self.view_todos()
            elif choice == "2":
                self.add_todo()
            elif choice == "3":
                self.complete_todo()
            elif choice == "4":
                self.delete_todo()
            elif choice == "5":
                self.search_todos()
            elif choice == "6":
                self.show_statistics()
            elif choice == "7":
                self.save_todos()
                print("Thank you for using Todo List App! Goodbye! 👋")
                break
            elif choice == "8":
                confirm = input("Exit without saving? (y/N): ").strip().lower()
                if confirm == "y":
                    print("Goodbye! 👋")
                    break
            else:
                print("Invalid choice! Please select 1-8.")
            
            # Pause before showing menu again
            input("\nPress Enter to continue...")


def simple_todo_demo():
    """A simpler version for demonstration."""
    print("Simple Todo Demo")
    print("================")
    
    todos = []
    
    while True:
        print("\n1. Add todo")
        print("2. Show todos")
        print("3. Complete todo")
        print("4. Quit")
        
        choice = input("Choose: ")
        
        if choice == "1":
            task = input("Enter task: ")
            todos.append({"task": task, "done": False})
            print("Added!")
        
        elif choice == "2":
            if not todos:
                print("No todos!")
            else:
                print("\nYour todos:")
                for i, todo in enumerate(todos, 1):
                    status = "✅" if todo["done"] else "⏳"
                    print(f"{i}. {status} {todo['task']}")
        
        elif choice == "3":
            if not todos:
                print("No todos to complete!")
            else:
                try:
                    num = int(input("Which todo number? "))
                    if 1 <= num <= len(todos):
                        todos[num-1]["done"] = True
                        print("Completed!")
                    else:
                        print("Invalid number!")
                except ValueError:
                    print("Enter a valid number!")
        
        elif choice == "4":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    print("Todo List Application")
    print("=====================")
    print()
    print("Choose version:")
    print("1. Full-featured Todo App")
    print("2. Simple Demo Version")
    
    version = input("Enter choice (1 or 2): ").strip()
    
    if version == "1":
        app = TodoApp()
        app.run()
    elif version == "2":
        simple_todo_demo()
    else:
        print("Invalid choice! Running full app...")
        app = TodoApp()
        app.run()
