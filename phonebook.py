phonebook = {}

def add_contact(name, number):
    phonebook[name] = number
    print("Contact added successfully.")

def search_contact(name):
    if name in phonebook:
        print(f"Name: {name} \t Number: {phonebook[name]}")
    else:
        print("Contact not found.")

def update_contact(name, number):
    if name in phonebook:
        phonebook[name] = number
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact(name):
    if name in phonebook:
        del phonebook[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

# Main loop
while True:
    print("PhoneBook App")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        name = input("Enter contact name: ")
        number = input("Enter contact number: ")
        add_contact(name, number)

    elif choice == "2":
        name = input("Enter contact name: ")
        search_contact(name)

    elif choice == "3":
        name = input("Enter contact name: ")
        if name in phonebook:
            number = input("Enter new number: ")
            update_contact(name, number)
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter contact name: ")
        delete_contact(name)

    elif choice == "5":
        print("Exiting PhoneBook, Goodbye")
        break
    else:
        print("Invalid input")