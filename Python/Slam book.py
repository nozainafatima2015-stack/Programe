slam_book = []
slam_book = []   # List to store all entries

def add_entry():
    print("\n--- Add New Entry ---")
    name = input("Name: ")
    nickname = input("Nickname: ")
    fav_color = input("Favourite Color: ")
    fav_food = input("Favourite Food: ")
    hobby = input("Hobby: ")
    message = input("Message for your friend: ")

    entry = {
        "name": name,
        "nickname": nickname,
        "fav_color": fav_color,
        "fav_food": fav_food,
        "hobby": hobby,
        "message": message
    }

    slam_book.append(entry)
    print("Entry added!\n")

def view_entries():
    if not slam_book:
        print("\nNo entries yet.\n")
        return
print("\n--- Slam Book Entries ---")
for i, e in enumerate(slam_book,1):
        print(f"\nEntry #{i}:")
        print(f"Name: {e['name']}")
        print(f"Nickname: {e['nickname']}")
        print(f"Favourite Color: {e['fav_color']}")
        print(f"Favourite Food: {e['fav_food']}")
        print(f"Hobby: {e['hobby']}")
        print(f"Message: {e['message']}")
        print()
found = True
 

if not found:
    print("No entry found with that name.\n")

# -------- Program Menu ---------

while True:
    print("Slam Book Menu")
    print("1. Add Entry")
    print("2. View All Entries")
    print("3. Search Entry")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_entry()
    elif choice == "2":
        view_entries()
    elif choice == "3":
        search_entry(your_name)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.\n")
        print("****************************************************************************************")
        print("/t/t/SMARTPHONE DIRECTORY", flush=False)
        print("****************************************************************************************")
        print("Now you can perform the following operations on this phonebook/n")
        print("1. Add a new contact")
        print("2. Remove an existing contact")
        print("3. Delete all contacts")
        print("4. Search for a contact")
        print("5. Display all contacts")
        print("6. Exit phonebook")
        choice = int(input("Please enter your choice: ")) 
return choice
def add_contact(pd):
    dip=[]
    for i in range(len(pd[0])):
        if i == 0:  
            dip.append(str(input("Eneter name*:")))
    if i == 1: 
        dip.append(int(input("Enter number: "))) 
    if i == 2: 
        dip.append(str(input("Enter e-mail address: "))) 
    if i == 3: 
        dip.append(str(input("Enter date of birth(dd/mm/yy): "))) 
    if i == 4: 
        dip.append( 
				str(input("Enter category(Family/Friends/Work/Others): "))) 
    pb.append(dip) 
    return pb

    def thanks():
        print("Thank you for using the phonebook. Goodbye!")
        print("****************************************************************************************")
        print("Thankyou for using the phonebook.")
        print("Please visit again.")
        print("****************************************************************************************")
        sys.exit("Goodbye, have a nice day!")
        print("....................................................................................................")
        print(" Hello dearfriends . Welcome to our slam book .")
        print("You may now proceed to explore this slambook and fill your details about your friend.")
        print("....................................................................................................")
        print("You may now proceed to explore this slambook and fill your details about your friend.")
        print("....................................................................................................")
        ch = 1
        pd = initial_slambook()
        while ch in(1, 2, 3, 4, 5):
            ch = menu()
            if ch == 1:
                pd = add_contact(pd)
            elif ch == 2:
                pd = add_contact(pd)
            else:
                thanks()