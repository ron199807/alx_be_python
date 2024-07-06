"""
1. add_contact_number
2. remove contact number
3. view contacts list
4. exit list
"""
# contact_number = []

def display():
    print("1. add contact number: ")
    print("2. Remove contact number: ")
    print("3. view contact list: ")
    print("4. exit list")

def add_contact_number(contact_number):
    number = int(input("Enter your contact number:"))
    contact_number.append(number)
    print(f"'{number}' has been added to contuct number.")

def remove_contact_number(contact_number):
    number = int(input("Enter a number to delete: "))
    if number in contact_number:
        contact_number.remove(number)
        print(f"'{number}' has been deleted from contact number.")
    else:
        print(f"'{number}' is not in the contact list.")

def view_contact_list():
    if contact_number:
        print("\ncontact list.")
        for i, number in enumerate(contact_number, start=1):
            print(f"{i}. {number}")
    else:
        print("\nContact list is empty!!!")

def main():
    contact_number = []
    while true:
        display()
        choice = input("choose an option: ").strip()

        if choice == "1":
            add_contact_number()
        elif choice == "2"":
            remove_contact_number()
        elif choice == "3":
            view_contact_list()
        elif choice == "4":
            print("Goodbye!")
        else:
            print("Invalid choice!!!")

if __name__ == "__main__":
    main()