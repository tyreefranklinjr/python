cat << 'EOF' > README.md
# Expense Tracker

## Overview

The Expense Tracker is a command-line Python application designed to help users track expenses, analyze spending habits, and manage financial activity.

This project demonstrates core programming concepts while simulating a real-world financial tracking tool.

---

## Features

- Add new expenses with name, amount, and category
- View all recorded expenses
- Display total spending (negative transactions)
- View total spending by category
- Sort expenses from lowest to highest
- Interactive CLI menu system
- Input validation for user selections

---

## Technologies Used

- Python
- Command-line interface (CLI)
- File handling concepts
- Data structures (lists and dictionaries)
- Exception handling

---

## Skills Demonstrated

- Working with lists, dictionaries, and numerical data
- Organizing and categorizing data dynamically
- Sorting algorithms and logic implementation
- Looping and conditional control flow
- User input validation and interaction
- Modular function design

---

## How It Works

1. The application starts with a menu of options (1–6)
2. Users can:
   - Add expenses with a name, amount, and category
   - View all expenses entered
   - Analyze total spending
   - Break down expenses by category
   - Sort expenses by amount
3. Data is stored in memory using lists and dictionaries during runtime

---

## Example Expense Format

```
{"name": "Burgers", "amount": -5.99, "category": "Dining"}
```

---

## Running the Program

1. Make sure Python is installed
2. Run the script:

```
python expense_tracker.py
```

---

## Notes

- Expenses are stored temporarily in memory during runtime
- Negative values represent spending
- Category tracking is dynamically built as expenses are added
- Sorting is implemented manually for learning purposes

---

## Future Improvements

- Save and load expenses from files (JSON/CSV)
- Improve sorting algorithm efficiency (use built-in sorting)
- Add data visualization (charts/graphs)
- Implement monthly summaries and budgeting
- Improve category matching logic
- Add input validation for cleaner data entry

---

## Author

**Tyree Franklin Jr.**

---

## Goal

This project was built to strengthen Python fundamentals and demonstrate the ability to build real-world CLI applications focused on data tracking and analysis.
EOF
