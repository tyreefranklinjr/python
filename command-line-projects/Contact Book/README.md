# Contact Book App

## Overview

The Contact Book App is a command-line Python application that allows users to manage personal contacts efficiently.

Users can add, view, update, delete, and load contacts from a file, making it a practical project for learning core programming concepts and file handling.

---

## Features

- Add new contacts (name, phone, email)
- View all saved contacts
- Update existing contact information
- Delete contacts
- Load contacts from a file
- Input validation for user selections
- Clean terminal interface

---

## Technologies Used

- Python
- Command-line interface (CLI)
- File handling (`with open`)
- Object-oriented programming (classes)
- Exception handling

---

## Skills Demonstrated

- Use of classes and object-to-dictionary conversion
- Lists and dictionaries for data storage
- File reading and error handling
- Loops and conditionals
- Input validation and user interaction
- String manipulation and formatting

---

## How It Works

1. The program runs in a loop until the user chooses to quit
2. A menu is displayed with options (1–6)
3. Users select an option to perform actions such as:
   - Adding a contact
   - Viewing all contacts
   - Updating or deleting a contact
   - Loading contacts from a file
4. Contacts are stored in a list of dictionaries during runtime

---

## Example Contact Format

```
{"name": "Tyree", "phone": "1234567890", "email": "example@gmail.com"}
```

---

## Running the Program

1. Make sure Python is installed
2. Run the script:

```
python contact_book.py
```

---

## Notes

- Contacts are stored in memory unless loaded from a file
- File loading expects each line to contain a dictionary format
- Uses `eval()` for parsing (can be improved for security in future versions)

---

## Future Improvements

- Save contacts to a file automatically
- Replace `eval()` with safer parsing (e.g., JSON)
- Add search functionality
- Improve UI/UX formatting
- Add input validation for phone/email formats

---

## Author

**Tyree Franklin Jr.**

---

## Goal

This project was built to strengthen Python fundamentals and demonstrate the ability to build interactive CLI applications with real-world functionality.
