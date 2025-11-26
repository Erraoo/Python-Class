SALES_TAX = 0.0945
menu = [0, "King Cake Slice", "Croissant", "Catfish Po-boy", "Roast Beef Po-boy", "Sausage Po-boy", "Gumbo", "Crawfish Pie"]
price = [0, 4.95, 3.95, 14.95, 13.95, 12.95, 5.95, 3.65]

finish = False
total = 0

def title():
    print("Boudreaux & Thibodeaux's Restaurant")
    print(f"1. {menu[1]}: ${price[1]} \n2. {menu[2]}: ${price[2]} \n3. {menu[3]}: ${price[3]} \n4. {menu[4]}: ${price[4]} \n5. {menu[5]}: ${price[5]} \n6. {menu[6]}: ${price[6]} \n7. {menu[7]} (By the Slice): ${price[7]}")

def crawfish(quantity):
    crawfish_pie_cost = 22
    crawfish_slice_cost = 3.65
    pie = 0
    slice = 0
    pie_subtotal = 0
    slice_subtotal = 0
    pie_total = 0
    slice_total = 0
    pie_tax = crawfish_pie_cost * SALES_TAX
    slice_tax = crawfish_slice_cost * SALES_TAX


    while quantity != 0:
        if quantity >= 8:
            quantity -= 8
            pie += 1
        elif quantity != 0 and quantity < 8:
            quantity -= 1
            slice += 1

    if pie > 0:
        pie_subtotal = crawfish_pie_cost * pie
        pie_total = pie_subtotal + pie_tax
    if slice > 0:
        slice_subtotal = crawfish_slice_cost * slice
        slice_total = slice_subtotal + slice_tax

    print(f"You have ordered {pie} Crawfish Pie for ${pie_subtotal:.2f}.")
    print(f"You have ordered {slice} Crawfish Slice for ${slice_subtotal:.2f}")
    return pie_total or slice_total


title()
while finish != True:
    food = (input("What would you like to order? Please type a number from the menu item or type DONE when order is complete: "))
    if food.upper() == "DONE":
        finish = True
    else:
        try:
            food = int(food)
            if food < 1 or food > 7:
                print("Invalid input. Please try again.")
                title()
            elif food == 7:
                food = int(food)
                quantity = int(input("How many of that item would you like to order? "))
                total += crawfish(quantity)
            elif food >= 1 and food <= 6:
                food = int(food)
                quantity = int(input("How many of that item would you like to order? "))
                print(f"You have ordered {quantity} {menu[food]}(s) for ${price[food]} each.")
                total = (quantity * float(price[food])) + (quantity * (SALES_TAX * float(price[food])))
                title()
        except:
            print("Invalid input. Please try again.")
            title()
print(f"Your total is ${total:.2f}")