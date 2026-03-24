import time

item_id = 1
products = [["1", "chips", 15, "solid", "20g", 12]]

def start():
    print("\nWelcome to Inventory Manager")
    print("1. View items\n2. Add item\n3. Remove item\n4. Update item\n5. Search item\n6. Exit")
    choice = int(input("Enter choice: "))
    if choice == 1: print_items()
    elif choice == 2: add()
    elif choice == 3: remove()
    elif choice == 4: update()
    elif choice == 5: search()
    elif choice == 6: print("Thank you!"); return
    else: print("Invalid choice."); time.sleep(1)
    start()

def print_items():
    print("All items:")
    for item in products:
        print("|".join(map(str, item)))
    input("Press enter..."); start()

def add():
    global item_id
    print(f"Adding item ID: {item_id}")
    name = input("Name: ")
    qty = int(input("Quantity: "))
    typ = input("Type: ")
    weight = input("Weight: ")
    price = float(input("Price: "))
    products.append([str(item_id), name, qty, typ, weight, price])
    item_id += 1
    print("Added!"); input("Press enter..."); start()

def search():
    name = input("Search name: ")
    for item in products:
        if item[1] == name:
            print(item); input("Press enter..."); start()
    print("Not found."); input("Press enter..."); start()

def update():
    name = input("Update name: ")
    for i, item in enumerate(products):
        if item[1] == name:
            products[i][1] = input("New name: ")
            products[i][2] = int(input("New qty: "))
            products[i][3] = input("New type: ")
            products[i][4] = input("New weight: ")
            products[i][5] = float(input("New price: "))
            print("Updated!"); input("Press enter..."); start()
    print("Not found."); input("Press enter..."); start()

def remove():
    name = input("Remove name: ")
    for i, item in enumerate(products):
        if item[1] == name:
            del products[i]; print("Removed!"); input("Press enter..."); start()
    print("Not found."); input("Press enter..."); start()

start()
