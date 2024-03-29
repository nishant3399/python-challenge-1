# Python Challenge 1
## Menu
print("Welcome to Nishant's Food Truck")
print()

menu_items = ["Hamburger", "Cheeseburger", "French Fries", "Milkshake", "I'm done ordering"]
menu_prices = [7.00, 9.00, 5.00, 6.00, "NA"]

for n in range(len(menu_items)):
    print(str(n+1) + ' ' + menu_items[n], menu_prices[n], sep='\t')

print()
menu_selection = int(input("Enter your option: "))

subtotal = 0  # Initialize subtotal

while menu_selection != 5:
    if 1 <= menu_selection <= 4:  # Check if option is valid
        quantity = int(input("How many " + menu_items[menu_selection - 1] + "s would you like? "))
        total_price = menu_prices[menu_selection - 1] * quantity
        print("Subtotal for", quantity, menu_items[menu_selection - 1] + "(s): $" + str(total_price))
        subtotal += total_price  # Add current item price to subtotal
        
    else:
        print("Invalid option")

    print()
    menu_selection = int(input("Enter your option: "))

print("Thank you for your order!")
print("Your total bill is: $" + str(subtotal))

