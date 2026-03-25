# Tyree Franklin Jr.
# Contact Book App
# This is a simple command-line app where the user can:
#   add contacts, search contacts, update contacts,
#   delete contacts, and save/load contacts from file

# It includes skills such as:
#    dictionary lists, file handling with 'with', exceptions,
#    functions, loops, searching, string methods like '.lower()',
#    sorting alphabetically


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
        print("Contact Book App\n")
        print("Incorrect input!\n")
        print("Enter the following to get started (1-6)\n")
        print("1. Add Contact\n2. View Contacts\n3. Update Contact\n4. Delete Contact\n5. Load Contact from file\n6. Quit\n")
        choice = int(input("Input: "))
    
# {"name": Tyree, "phome": 1234567890, "email": "tyree.franklinjr@gmail.com"}

class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }

# Get the user input
clear_screen()
section()

running = True
contacts = []

while running:

    print("\nContact Book App\n")
    print("Enter the following to get started (1-6)\n")
    print("1. Add Contact\n2. View Contacts\n3. Update Contact\n4. Delete Contact\n5. Load Contact from file\n6. Quit\n")
    choice = int(input("Input: "))
    
    input_validation(choice)

    if choice == 1:
        clear_screen()
        section()
        print("Add Contact\n")
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")

        contact = Contact(name, phone, email)
        contacts.append(contact.to_dict())

    elif choice == 2:
        clear_screen()
        section()
        print("View Contact\n")
        count = 1

        for contact in contacts:
            name = contact["name"]
            phone = contact["phone"]
            email = contact["email"]
            
            print(f"{count}. {name} | {phone} | {email}")
            count += 1

            print()

    elif choice == 3:
        clear_screen()
        section()
        print("Update Contact\n")
        print("Choose the contact that you'd like to modify: \n")
        count = 1

        for contact in contacts:
            name = contact["name"]
            phone = contact["phone"]
            email = contact["email"]
            
            print(f"{count}. {name} | {phone} | {email}")
            count += 1

        print("Select a contact you'd like to modify.\n")
        selection = int(input("Input: "))

        if selection < 0 or selection > len(contacts):
            print("Incorrect input!")
            break
        else:
            object = contacts[selection - 1]

            print("\nWhat would you like to change it to?\n")
            object["name"] = input("Name: ")
            object["phone"] = input("Phone: ")
            object["email"] = input("Email: ")

            print("\nFixed!")
        
    elif choice == 4:
        clear_screen()
        section()
        print("Delete Contact\n")
        print("Please enter the # of the contact \nthat you'd like to delete\n")

        count = 1

        for contact in contacts:
            name = contact["name"]
            phone = contact["phone"]
            email = contact["email"]
            
            print(f"{count}. {name} | {phone} | {email}")
            count += 1

        selection = int(input("\nInput: "))

        del contacts[selection - 1]

        print("\nDeleted!")

    elif choice == 5:
        clear_screen()
        section()
        print("Open File Data\n")
        print("Enter the name of the file you would like to open\n")
        file_name = input("File: ")

        try:
            with open(file_name, 'r') as file:
                for line in file:
                    line = line.strip()

                    if line:
                        contact = eval(line)
                        contacts.append(contact)
                print("\nContacts loaded successfully!")

        except FileNotFoundError:
            print(f"Error: The file '{file_name}' was not found.")
            
        except IOError:
            print(f"Error reading the file '{file_name}'.")
             
    elif choice == 6:
        clear_screen()
        section()
        print("Thank you for using our app, see you later!")
        running = False
