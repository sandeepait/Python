doubles = [x*2 for x in range(1, 11)]
tripples = [x*3 for x in range(1, 11)]
squares = [x*x for x in range(1, 11)]
fruits = ["apple", "banana", "cherry","mango", "strawberry"]
numbers = [-1, 0, -4, -100, 300, 40, 2, 98, -89, -7]

print(doubles)
print(tripples)
print(squares)

fruit_chars=[fruit[0] for fruit in fruits]
print(fruit_chars)

positive_Numbers= [num for num in numbers if num>=0]
print(positive_Numbers)

negative_Numbers= [num for num in numbers if num<0]
print(negative_Numbers)

even_Numbers= [num for num in numbers if num%2==0]
print(even_Numbers)

odd_Numbers= [num for num in numbers if num%2==1]
print(odd_Numbers)