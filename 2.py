# Function to add items to the grocery list
def add_items_to_list(grocery_list):
    while True:
        item_to_add = input("What item do you want to add? ")
        grocery_list.append(item_to_add)
        print_list(grocery_list, "Your grocery list has the following items in it:")
        answer = input("Add another item? (y/n) ")
        if answer.lower() == "n":
            break

# Function to print the grocery list
def print_list(grocery_list, message):
    print(message)
    print("-----")
    for item in grocery_list:
        print("- " + item)
    print("-----")

# Function to remove items from the grocery list
def remove_items_from_list(grocery_list, removed_items):
    while True:
        item_to_remove = input("Enter the item you want to remove: ")
        if item_to_remove in grocery_list:
            removed_items.append(item_to_remove)  # Add to removed items list
            grocery_list.remove(item_to_remove)
            print(item_to_remove + " has been removed from the list.")
        else:
            print("Item not found in the list.")
        another_removal = input("Do you want to remove another item? (y/n) ")
        if another_removal.lower() != "y":
            break

# Main function to execute the grocery list program
def main_grocery_list():
    grocery_list = []
    removed_items = []  # To store removed items

    add_items_to_list(grocery_list)
    print_list(grocery_list, "Your final grocery list is:")

    remove_items = input("Do you want to remove any items? (y/n) ")
    if remove_items.lower() == "y":
        remove_items_from_list(grocery_list, removed_items)

    print_list(grocery_list, "Your updated grocery list is:")
    
    print("Items removed:")
    print("-----")
    for item in removed_items:
        print("- " + item)
    print("-----")

# Run the grocery list program
main_grocery_list()
