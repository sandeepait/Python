# This is a sample Python script.
from typing import Any


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    age = 100
    price = 20.45
    is_online = True
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print("age:", age)
    print("price:", price)
    print("is_online:", is_online)

    name = input("What is your name? ")

    print("Hello " + name)

    birth_year = int(input("Enter your birth year: "))

    print("Your age: ", 2026-birth_year)

    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))

    print("Sum: ", str(round(first_number + second_number, 2)))

    course = "Python for Beginners"

    print(course.lower())

    print(course.find("or"))

    print("Python" in course)

    print(34 / 10)
    print(34 // 10)
    print(34 % 10)
    print(34 ** 10)
    age += 3
    print("augmented age: ", age)

def logical_operators():

    price = int(input("Enter your price: "))

    print(price > 100 and price < 200)
    print(100 < price < 200)
    print(price>100 or price<200)
    print( not(price > 100 or price < 200))

def if_statement():

    temperature = int(input("Enter your temperature: "))

    if temperature >= 30:
        print("It's a hot day")
    elif 20 < temperature < 30:
        print("It's a nice day")
    else:
        print("It's a cold day")

    print("if block is done")

def while_loop():

    i=0
    while i<10:
        print(i*"*")
        i+=1

def list_type():
    names = ["name1", "name2", "name3", "name3", "name3", "name3"]
    print(names)
    print(type(names))
    print(names[0:2])
    names[2] = "Raj"
    print(names)

    names.append("Simran")
    print(names)

    names.insert(0,"Myself")
    print(names)

    print("Raj" in names)
    print( len(names))

    names.remove("name3")
    print(names)

    for item in names:
        print(item)

    numbers = range(0, 10, 2)
    for item in numbers:
        print(item)

    for item in range(0, 10, 3):
        print(item)

    # print in reverse
    print(names[::-1])

    print(int(names.index("name3")))
    print(names.count("name3"))


def nested_loops():

    rows = int(input("Enter the numer of rows: "))
    columns = int(input("Enter the number of columns: "))
    symbol = input("Enter the symbol: ")

    for x in range(rows):
        for i in range(columns):
           print(symbol, end="")
        print()

def set_type():
    fruits = {"apple", "banana", "cherry"}
    print(fruits)

    #pop removes first element
    fruits.pop()
    print(fruits)
def tuple_type():
    fruits = ("apple", "banana", "cherry", "apple", "banana", "cherry", "cherry")
    print(fruits)
    print(fruits.index("apple"))
    print(fruits.count("cherry"))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #print_hi('PyCharm')
    #logical_operators()
    #if_statement()
    #while_loop()
    #List = [] orderded and changeable Duplicates fine
    #set = {} unordered and immutable Add/Remove is ok No duplicates
    #tuple = () ordered and unchangeable Duplicates ok, Faster than lists
    #list_type()
    #set_type()
    tuple_type()
    #nested_loops()
