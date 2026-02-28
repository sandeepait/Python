numbers = [1, 2, 3, 4, 5]

for number in numbers:
    print(number, end=" ")

print("\n")
for number in reversed(numbers):
    print(number, end=" ")
print("\n")

fruits = ["apple", "banana", "cherry", "grape", "mango"]
for fruit in fruits:
    print(fruit, end=" ")

print("\n")

name = "Alexander the great"

for letter in name:
    print(letter, end=" ")

print("\n")

my_dict = {
    "name": "Alexander the great",
    "age": 30,
    "city": "San Francisco",
    "Occupation": "Mayor",
    "Skil": "nothing"
}

for key in my_dict.keys():
    print(key, end=" ")
print("\n")
for value in my_dict.values():
    print(value, end=" ")
print("\n")
for key, value in my_dict.items():
    print(f"{key}: {value}")
print("\n")