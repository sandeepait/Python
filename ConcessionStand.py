menu = {"Pizza" : 3.59,
        "PopCorn": 4.59,
        "Samosa": 1.59,
        "fries": 2.00,
        "pretzel": 4.25,
        "soda": 2.30,
        "lemonade": 1.49,
        "nachos": 2.00}

cart = []
total = 0

print("*******Menu*******")
for key, value in menu.items():
    print(f"{key:8} : ${value:.2f}")

print("*******************")

while True:
    choice = input("Please select and item(q to quit): ")
    if choice.upper() == "Q":
        break
    elif menu.get(choice) is not None:
        cart.append(choice)
        total += menu.get(choice)
    else:
        print("Invalid choice. Please try again.")


print("---------Your Order------------")
for item in cart:
    print(item, end=" ")
print()
print(f"You Pay: {total}")
