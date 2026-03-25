# Tyree Franklin Jr.
# Quiz Game
# This is a simple command-line app where the user can:
#   prompt questions, grade quizzes, and check answers

# It includes skills such as:
#   dictionaries, lists, loops, functions, string methods,
#   and conditionals

import os

# Declare the essential functions
def clear_screen():
    if os.name == "nt":
        _ = os.system('cls')
    else:
        _ = os.system("clear")

def section():
    print("--------------------------------------")

# User input validation for the start menu
def start_validation(selection):
    while selection != 'x' and selection != 's':
        print("Incorrect input!\nEnter 's' to start and 'x' to exit the quiz: \n")
        selection = input("Input: ")
    if selection == 'x':
        return 'x'
    if selection == 's':
        return 's'

# Questions list with each tempalate in the form of a dictionary
questions = [
  {
    "question": "Who created the Python programming language?",
    "choices": ["A. Dennis Ritchie", "B. James Gosling", "C. Guido van Rossum", "D. Bjarne Stroustrup"],
    "answer": "C"
  },
  {
    "question": "In what year was Python first released?",
    "choices": ["A. 1985", "B. 1991", "C. 1999", "D. 2005"],
    "answer": "B"
  },
  {
    "question": "Python was named after which British comedy group?",
    "choices": ["A. The Beatles", "B. Monty Python", "C. The Goon Show", "D. The Young Ones"],
    "answer": "B"
  },
  {
    "question": "Which organization originally hosted Python's development before it moved to the Python Software Foundation?",
    "choices": ["A. Google", "B. Microsoft", "C. Centrum Wiskunde & Informatica (CWI)", "D. IBM"],
    "answer": "C"
  },
  {
    "question": "What major Python version introduced significant changes that were not fully backward compatible with Python 2?",
    "choices": ["A. Python 2.7", "B. Python 3.0", "C. Python 1.5", "D. Python 2.0"],
    "answer": "B"
  }
]

# Prompt the user's start menu
section()
print("Welcome to the Quiz Game")
print("Enter 's' to start and 'x' to exit the quiz: \n")
selection = input("Input: ")

choice = start_validation(selection)

clear_screen()
points = 0

# Running the quiz
if choice == 's':

  for question in questions:
    print(question["question"])

    options = question["choices"]
    print()

    for option in options:
      print(option)
    print()

    choice = input("Answer: ")
    print()

    if choice == question["answer"] or choice.upper == question["answer"]:
      points += 1
    
  # Output quiz results
  clear_screen()
  section()
  score = points / len(questions)
  print(f"Your score is: {score} / {len(questions)}")
  print(f"Your quiz grade is {score * 100}%")
  print(f"You got {points} questions correct.\n")

# Quit function
elif choice == 'x':
  clear_screen()
  section()
  print("Thank you for playing our game, see you next time!\n")
