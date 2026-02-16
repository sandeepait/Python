import string

MyString  = []
for i in range(3):
    MyString.append(input("Please enter a string: "))
for str in MyString:
    print(str, end="**")