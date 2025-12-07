import sys
def initial_phonebook():
    rows , cols=int(input("pleas eeter initial number of contacts:")),5
    phone_book=[]
    print(phone_book)
    for i in range(rows):
        print("/n Eneter %d details in the following order(ONLY):" % (i+1))
        print("NOTE: * indecate mandetary fields")
        print(".......................................................................................................")

Phone_book={}

while True:
    print("\n Phone Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        name = input("Enter Name*: ")
        phone = input("Enter Phone Number*: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")
        birthday = input("Enter Birthday: ")
        
        Phone_book[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address,
            "Birthday": birthday
        }
        print(f"Contact {name} added successfully.")
    
    elif choice == '2':
        if not Phone_book:
            print("Phone book is empty.")
        else:
            for name, details in Phone_book.items():
                print(f"\nName: {name}")
                for key, value in details.items():
                    print(f"{key}: {value}")
    
    elif choice == '3':
        search_name = input("Enter the name to search: ")
        contact = Phone_book.get(search_name)
        if contact:
            print(f"\nName: {search_name}")
            for key, value in contact.items():
                print(f"{key}: {value}")
        else:
            print(f"Contact {search_name} not found.")
    
    elif choice == '4':
        delete_name = input("Enter the name to delete: ")
        if delete_name in Phone_book:
            del Phone_book[delete_name]
            print(f"Contact {delete_name} deleted successfully.")
        else:
            print(f"Contact {delete_name} not found.")
    
    elif choice == '5':
        print("Exiting the phone book application.")
        sys.exit()
    
    else:
        print("Invalid choice. Please try again.")