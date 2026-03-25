# Tyree Franklin Jr.
# Expense Tracker
# This is a simple command-line app where the user can:
#   track expenses, analyze spending habits, and document financial activity

# It includes skills such as:
#    lists, numbers, dictionaries, sorting
#    file handling, exceptions, and sorting

import os

# Declare the essential functions

def clear_screen():
    if os.name == "nt":
        _ = os.system('cls')
    else:
        _ = os.system("clear")

def section():
    print("--------------------------------------")

def input_validation(selection):
    while selection < 1 or selection > 6:
        clear_screen()
        section()
        print("Expense Tracker")
        print("Incorrect input!")
        print("\nWelcome to the expense tracker, let's get started\nwith entering the following choices:\n")

        selection = int(input("\n1. Add Expense\n2. View all expenses\n3. Show total spent\n4. Category Totals\n5. Sort Expenses\n6. Quit\n\nInput: "))

# Get the user input
clear_screen()
section()
print("Expense Tracker")
print("\nWelcome to the expense tracker, let's get started\nwith entering the following choices:\n")

selection = int(input("\n1. Add Expense\n2. View all expenses\n3. Show total spent\n4. Category Totals\n5. Sort Expenses\n6. Quit\n\nInput: "))

input_validation(selection)

running = True
expenses = []
prices = []
categories = []
initial_run = True

# {"cat_name": "dining", "amaount": 52.99}
# {"name": "burgers", "amount": 5.99, "category": "dining"}

while running:

    # Repeat the app menu
    if not initial_run:
        print("Expense Tracker")
        print("\nWelcome to the expense tracker, let's get started\nwith entering the following choices:\n")

        selection = int(input("\n1. Add Expense\n2. View all expenses\n3. Show total spent\n4. Category Totals\n5. Sort Expenses\n6. Quit\n\nInput: "))

    initial_run = False

    # Add Expense
    if selection == 1:
        clear_screen()
        section()

        # Input data
        print("Add Expense\n")
        name = input("Expense name: ")
        amount = float(input("Amount (Include '-' for spending): "))
        category = input("Category (Ex. dining): ")
        
        new_expense = {"name": name, "amount": amount, "category": category}
        expenses.append(new_expense)
        prices.append(amount)

        # Organize the expense into categories
        category_template = {"category": category, "amount": amount}


        if len(categories) < 1:
            categories.append(category_template)
            print(category_template)

        else:
            
            identified = False
            for category_group in categories:

                if category == category_group:
                    print(category)
                    category_group["amount"] += amount
                    identified = True
                    break
            
            if identified == False:
                    categories.append(category_template)
                    print(categories)
                    
        clear_screen()
        section()
        print("Expenses added!\n")
        selection = None

    # View all expenses
    elif selection == 2:
        clear_screen()
        section()
        print("View All Expenses\n") 

        # Print the expenses
        count = 1
        for expense in expenses:
            name = expense["name"]
            amount = expense["amount"]
            category = expense["category"]
            
            print(f"{count}. {name}: {amount}, {category}")
            count += 1

        choice = input("\nEnter anything to continue to menu\n")
        clear_screen()

    # Show all negative expenses
    elif selection == 3:
        clear_screen()
        section()
        print("Show Total Spent\n")
        
        count = 1

        # Print the expenses
        for expense in expenses:
            name = expense["name"]
            amount = expense["amount"]
            category = expense["category"]
            
            if amount < 0:
                print(f"{count}. {name}: {amount}, {category}")
                count += 1

        choice = input("\nEnter anything to continue to menu\n")
        clear_screen()
    
    # View the total amount in each category
    elif selection == 4:
        clear_screen()
        section()
        print("Category Totals\n")

        # Print the catgeory names with the corresponding spending amount
        count = 1
        for category_group in categories:
            name = category_group["category"]
            amount = category_group["amount"]
            print(f"{count}. {name}: {amount}")
            count += 1

    # Sort expenses
    elif selection == 5:
        clear_screen()
        section()
        print("Sort Expenses (Low -> High)\n")

        # Sorting the prices that were added from 'Add Expenses' feature
        temp = 0
        prev = 0
        index = 0

        sorted_prices = prices
        duplicate_prices = prices

        # Sort duplicated list with amounts
        for price in sorted_prices:

            if index > 0:
                if price < prev:
                    temp = price
                    price = prev
                    sorted_prices[index - 1] = price
            else:
                price = prev
            index += 1

        count = 1
        index = 0

        # Print the calculated sorted prices
        for price in sorted_prices:
             
            for obj_price in duplicate_prices:

                if obj_price == price:
                    object = expenses[index]
                    name = object["name"]
                    amount = object["amount"]
                    category = object["category"]

                    print(f"{count}. {name}: {amount}, {category}")
                    break
                index += 1

            count += 1

    # Quit function
    elif selection == 6:
        
        clear_screen()
        section()
        print("Thank you for using our app, see you later!")
        running = False
