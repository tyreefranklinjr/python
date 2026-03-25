# To-Do List Manager

## Overview

The To-Do List Manager is a command-line Python application that allows users to manage daily tasks efficiently.

Users can add tasks, view them, mark them as complete, and delete them, making this a foundational project for learning core programming concepts and user interaction.

---

## Features

- Add new tasks
- View all tasks with completion status
- Mark tasks as complete
- Delete tasks
- Interactive CLI menu system
- Input validation for user selections

---

## Technologies Used

- Python
- Command-line interface (CLI)
- Lists and dictionaries
- Functions and modular design
- Control flow (loops and conditionals)

---

## Skills Demonstrated

- Managing data using lists and dictionaries
- Tracking state (complete vs incomplete tasks)
- Looping and conditional logic
- Function-based program structure
- User input handling and validation
- String formatting with f-strings

---

## How It Works

1. The program starts with a menu (0–4)
2. Users can:
   - Add tasks to the list
   - View all tasks with status (Complete/Incomplete)
   - Mark tasks as complete
   - Delete tasks
3. Tasks are stored in:
   - A list (for order)
   - A dictionary (for status tracking)
4. The program runs continuously until the user chooses to quit

---

## Example Task Output

```
1. Finish homework - Incomplete
2. Go to the gym - Complete
```

---

## Running the Program

1. Make sure Python is installed
2. Run the script:

```
python todo_list.py
```

---

## Notes

- Tasks are stored in memory during runtime
- Task status is tracked using a dictionary (`True` = Complete, `False` = Incomplete)
- Input validation ensures correct menu selection
- Designed for simplicity and clarity as a foundational project

---

## Future Improvements

- Save and load tasks from a file (JSON or text)
- Add due dates and priority levels
- Improve UI formatting
- Add search and filter functionality
- Prevent duplicate tasks
- Add persistent storage

---

## Author

**Tyree Franklin Jr.**

---

## Goal

This project was built to strengthen Python fundamentals and demonstrate the ability to build structured, interactive CLI applications with real-world use cases.
