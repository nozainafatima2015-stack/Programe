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