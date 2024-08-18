# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": 0.99,
        "Banana": 0.69,
        "Apple": 0.49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Initialize an empty list to store the customer's order.
order = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Continuous loop for placing an order
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order?")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first-level dictionary items in menu)
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Increment the menu item number
        i += 1

    # Get the customer's input for menu selection
    menu_selection = input("Type menu number: ")

    # 2. Input validation: Check if the customer's input is a number
    if menu_selection.isdigit():
        # Convert the menu selection to an integer
        menu_selection = int(menu_selection)

        # 3. Check if the menu selection is in the menu items
        if menu_selection in menu_items:
            # Get the category name from the menu_items dictionary
            menu_category_name = menu_items[menu_selection]
            print(f"You selected {menu_category_name}")

            # Print out the items in the selected category
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle sub-items differently
                if isinstance(value, dict):
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + " - " + key2)
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2:.2f}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value:.2f}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1

            # Ask the customer to input menu item number
            item_number = input("Type the item number you want to order: ")

            # 4. Input validation: Check if the customer's input is a number
            if item_number.isdigit():
                # Convert the item number to an integer
                item_number = int(item_number)

                # Check if the item number is in the menu items
                if item_number in menu_items:
                    # Get the item name and price from the menu_items dictionary
                    selected_item = menu_items[item_number]["Item name"]
                    item_price = menu_items[item_number]["Price"]

                    # Ask the customer for the quantity of the menu item
                    quantity = input(f"How many {selected_item} would you like to order? ")

                    # Input validation for quantity
                    if not quantity.isdigit():
                        quantity = 1
                    else:
                        quantity = int(quantity)

                    # Append the item, price, and quantity to the order list
                    order.append({
                        "Item name": selected_item,
                        "Price": item_price,
                        "Quantity": quantity
                    })

                    print(f"Added {quantity} {selected_item} to your order.")
                else:
                    print(f"{item_number} is not a valid item number.")
            else:
                print("You didn't select a valid item number.")
        else:
            print(f"{menu_selection} was not a valid menu option.")
    else:
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to keep ordering
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").strip().lower()

        # Use if-elif-else block instead of match-case
        if keep_ordering == 'y':
            place_order = True
            break
        elif keep_ordering == 'n':
            place_order = False
            print("Thank you for your order!")
            break
        else:
            print("Please type 'Y' or 'N'.")

# Print out the customer's order receipt
print("This is what we are preparing for you.\n")
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
for item in order:
    # 7. Save each dictionary item's key-value pair as a variable
    item_name = item["Item name"]
    item_price = item["Price"]
    item_quantity = item["Quantity"]

    # 8. Calculate the number of spaces for formatted printing
    num_item_spaces = 24 - len(item_name)
    num_price_spaces = 6 - len(f"${item_price:.2f}")

    # 9. Create space strings using string multiplication
    item_spaces = " " * num_item_spaces
    price_spaces = " " * num_price_spaces

    # 10. Print the item name, price, and quantity
    print(f"{item_name}{item_spaces} | ${item_price:.2f}{price_spaces} | {item_quantity}")

# 11. Calculate the total cost of the order using list comprehension and sum()
total_cost = sum(item['Price'] * item['Quantity'] for item in order)
print(f"\nTotal cost of your order: ${total_cost:.2f}")

# End of the script
print("Thank you for your order!")