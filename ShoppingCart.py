#shopping cart

foods = []
prices = []
total = 0

while True:
   food = input("Please enter food item: ")
   if food.upper() == "Q":
       break
   else:
       price = float(input("Please enter price for {food}:$ "))
       foods.append(food)
       prices.append(price)

print("_________Your Cart______")

for food in foods:
    print(food, end=" ")
print()
for price in prices:
    total = total + price

print("Your total is :$", total)

# Bro code 2:46