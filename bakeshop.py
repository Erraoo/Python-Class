SALES_TAX = 0.0945
menu = [0, "Muffin", "King Cake Slice", "Croissant", "Scone"]
price = [0, 5.95, 4.95, 3.95, 3.75]

print("Boudreaux & Thibodeaux's Bakery")

print(f"1. Muffin: ${price[1]}")
print(f"2. King Cake Slice: ${price[2]}")
print(f"3. Croissant: ${price[3]}")
print(f"4. Scone: ${price[4]}")

finish = False
total = 0

while finish != True:
    food = (input("What would you like to order? Please type a number from the menu item or type DONE when order is complete: "))
    if finish == True:
        print("DONE")
    elif food < "1" or food > "4":
        print("Invalid number. Please try again.")
    elif food >= "1" and food <= "4":
        food = int(food)
        quantity = int(input("How many of that item would you like to order? "))
        print(f"You have ordered {quantity} {menu[food]}(s) for ${price[food]} each.")
        total = (quantity * float(price[food])) + (quantity * (SALES_TAX * float(price[food])))
        total += total
else:
    print(f"Your total is ${total:.2f}")