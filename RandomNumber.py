import random

low = 1
high= 20
number = random.randint(low,high)
options = ("Rock", "Paper", "Scissors")
cards = ["2","3","4","5","6","7","8","10","J","Q","K","A"]

print(number)
number2 = random.random()
print(number2)

option = random.choice(options)
print(option)

print(cards)
random.shuffle(cards)
print(cards)