word="Apple"

letter=input("Enter a letter: ")

if letter in word:
    print(f"{letter} is in the word")
else:
    print(f"{letter} is not in the word")
print()


if letter not in word:
    print(f"{letter} is NOT in the word")
else:
    print(f"{letter} is IN the word")
print()

students = {"Spongebob", "Tom", "Jerry", "OnePiece", "Peppa"}

student=input("Enter a student: ")

if student in students:
    print(f"{student} is in the students list")
else:
    print(f"{student} is not in the students list")

grades = {
    "Spongebob": "A+",
    "Tom": "B+",
    "Jerry": "C+",
    "OnePiece": "D+",
    "Peppa": "E+",
}

if student in grades:
    print(f"{student} is in the grades list with {grades[student]}")
else:
    print(f"{student} is not in the grades list")

email="spongeb.ob@myemail.com"

if "@" in email and "." in email and email.count("@") == 1:
    print(f"Valid email address: {email}")
else:
    print(f"invalid {email} ")
