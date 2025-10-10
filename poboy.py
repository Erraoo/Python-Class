catfish_poboys = 14.95
roast_beef_poboys = 13.95
sausage_poboys = 12.95
gumbo = 4.95

sales_tax = 0.0945

print("Boudreaux & Thibodeaux's Po-Boy Shop")

print(f"1 Catfish Poboy: ${catfish_poboys}")
print(f"2 Roast Beef Poboy: ${roast_beef_poboys}")
print(f"3 Sausage Poboy: ${sausage_poboys}")
print(f"4 Gumbo: ${gumbo}")

print("Welcome! What would you like to order? (Please input only one menu item number):")
food = input()

if food == "1":
    total_cost = catfish_poboys + (catfish_poboys * sales_tax)
    print(f"Your total is ${total_cost:.2f}")
elif food == "2":
    total_cost = roast_beef_poboys + (roast_beef_poboys * sales_tax)
    print(f"Your total is ${total_cost:.2f}")
elif food == "3":
    total_cost = sausage_poboys + (sausage_poboys * sales_tax)
    print(f"Your total is ${total_cost:.2f}")
elif food == "4":
    total_cost = gumbo + (gumbo * sales_tax)
    print(f"Your total is ${total_cost:.2f}")
else:
    print("Invalid Response. Please select again.")