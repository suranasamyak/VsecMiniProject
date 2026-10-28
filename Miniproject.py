# Lost and Found Management System

lost_items = []
found_items = []


def add_lost_item():
    print("\n--- Add Lost Item ---")

    name = input("Enter item name: ")
    description = input("Enter description: ")
    location = input("Where was it lost? ")
    owner = input("Enter owner name: ")

    item = {
        "name": name,
        "description": description,
        "location": location,
        "owner": owner
    }

    lost_items.append(item)
    print("Lost item added successfully!")


def add_found_item():
    print("\n--- Add Found Item ---")

    name = input("Enter item name: ")
    description = input("Enter description: ")
    location = input("Where was it found? ")
    finder = input("Enter finder name: ")

    item = {
        "name": name,
        "description": description,
        "location": location,
        "finder": finder
    }

    found_items.append(item)
    print("Found item added successfully!")


def show_lost_items():
    print("\n--- Lost Items ---")

    if len(lost_items) == 0:
        print("No lost items found.")
    else:
        for i, item in enumerate(lost_items, 1):
            print("\nItem", i)
            print("Name:", item["name"])
            print("Description:", item["description"])
            print("Location:", item["location"])
            print("Owner:", item["owner"])


def show_found_items():
    print("\n--- Found Items ---")

    if len(found_items) == 0:
        print("No found items available.")
    else:
        for i, item in enumerate(found_items, 1):
            print("\nItem", i)
            print("Name:", item["name"])
            print("Description:", item["description"])
            print("Location:", item["location"])
            print("Finder:", item["finder"])


def search_item():
    print("\n--- Search Item ---")

    search = input("Enter item name to search: ").lower()

    found = False

    for item in lost_items:
        if search in item["name"].lower():
            print("\nLost Item Found:")
            print(item)
            found = True

    for item in found_items:
        if search in item["name"].lower():
            print("\nFound Item:")
            print(item)
            found = True

    if not found:
        print("Item not found.")


while True:

    print("\n==============================")
    print(" LOST AND FOUND MANAGEMENT SYSTEM")
    print("==============================")
    print("1. Add Lost Item")
    print("2. Add Found Item")
    print("3. Show Lost Items")
    print("4. Show Found Items")
    print("5. Search Item")
    print("6. Exit")
    print("==============================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_lost_item()

    elif choice == "2":
        add_found_item()

    elif choice == "3":
        show_lost_items()

    elif choice == "4":
        show_found_items()

    elif choice == "5":
        search_item()

    elif choice == "6":
        print("Thank you for using Lost and Found Management System!")
        break

    else:
        print("Invalid choice. Please try again.")