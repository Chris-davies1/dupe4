#Christian Davies
#CBIS 4210
#Assignment 01-03 - Inventory Management System

#add an item to inventory
def add_to_inventory(inventory, item_name, quantity):
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity
    print(f"Added {quantity} of {item_name} to inventory.")

#display the current inventory
def display_inventory(inventory):
    print("\nCurrent Inventory:")
    for item_name, quantity in inventory.items():
        print(f"{item_name}: {quantity}")
    print("\n")
#main function to start the inventory management system
def main():
    inventory = {}
    while True:
        print("Inventory Management System")
        print("1. Add item to inventory")
        print("2. Display inventory")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")
#add item to inventory
        if choice == '1':
            item_name = input("Enter the item name: ")
            quantity = int(input("Enter the quantity: "))
            add_to_inventory(inventory, item_name, quantity)
#display current inventory
        elif choice == '2':
            display_inventory(inventory)
#exit the system
        elif choice == '3':
            print("Exiting the Inventory Management System.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
#run the main function
if __name__ == "__main__":
    main()
