fruits = ["apple", "banana", "cherry"]
vegetables = ["celery", "potatoes", "cabbage"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

print(fruits)
print(vegetables)
print(meats)
print(groceries)
print(groceries[0])
print(groceries[1])
print(groceries[2])

for grocery in groceries:
    for g1 in grocery:
        print(g1, end=" ")
    print()
