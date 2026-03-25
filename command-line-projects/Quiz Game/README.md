# Quiz Game

## Overview

The Quiz Game is a command-line Python application that allows users to test their knowledge through a series of multiple-choice questions.

This project demonstrates fundamental programming concepts while building an interactive and engaging CLI-based experience.

---

## Features

- Start or exit menu system
- Multiple-choice quiz questions
- Real-time answer input
- Automatic grading system
- Final score and percentage display
- Clean terminal interface

---

## Technologies Used

- Python
- Command-line interface (CLI)
- Lists and dictionaries
- Control flow (loops and conditionals)

---

## Skills Demonstrated

- Working with lists of dictionaries (data modeling)
- Looping through structured data
- Conditional logic for answer checking
- User input validation
- String handling and formatting
- Building interactive CLI applications

---

## How It Works

1. The program prompts the user to start (`s`) or exit (`x`)
2. If started:
   - Each question is displayed with multiple-choice answers
   - The user inputs their answer
   - The program checks correctness and tracks points
3. After all questions:
   - Final score is calculated
   - Percentage grade is displayed
4. If exited:
   - Program closes with a message

---

## Example Question Format

```
{
  "question": "Who created Python?",
  "choices": ["A. Dennis Ritchie", "B. Guido van Rossum", "C. James Gosling", "D. Bjarne Stroustrup"],
  "answer": "B"
}
```

---

## Running the Program

1. Make sure Python is installed
2. Run the script:

```
python quiz_game.py
```

---

## Notes

- Answers are case-insensitive (handles uppercase input)
- Questions are stored as dictionaries for easy scalability
- Scoring is based on total correct answers divided by total questions

---

## Future Improvements

- Add more question categories
- Randomize question order
- Add timer functionality per question
- Store high scores
- Improve input validation (handle invalid answers better)
- Add difficulty levels

---

## Author

**Tyree Franklin Jr.**

---

## Goal

This project was built to strengthen Python fundamentals and demonstrate the ability to build interactive applications using structured data and logic.
