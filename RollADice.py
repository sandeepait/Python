import random

#print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")

# ● ┌ ─ ┐ │ └ ┘
"┌---------┐"
"│         │"
"│         │"
"│         │"
"└---------┘"

dice_art = {
            1:("┌---------┐",
               "│         │",
               "│    ●    │",
               "│         │",
               "└---------┘"),
            2:("┌---------┐",
               "│  ●      │",
               "│         │",
               "│       ● │",
               "└---------┘"),
            3:("┌---------┐",
               "│  ●      │",
               "│    ●    │",
               "│       ● │",
               "└---------┘"),
            4:("┌---------┐",
               "│  ●    ● │",
               "│         │",
               "│  ●    ● │",
               "└---------┘"),
            5:("┌---------┐",
               "│  ●    ● │",
               "│    ●    │",
               "│  ●    ● │",
               "└---------┘"),
            6: ("┌---------┐",
                "│  ●    ● │",
                "│  ●    ● │",
                "│  ●    ● │",
                "└---------┘")
}

dice = []
total = 0
number_of_dice = int(input("How many dice? "))

for i in range(number_of_dice):
    dice.append(random.randint(1, 6))
print(dice)

for i in range(number_of_dice):
    for j in dice_art.get(dice[i]):
        print(j)

for i in range(5):
    for die in dice:
        print(dice_art.get(die)[i], end="")
    print()

for d in dice:
    total+=d

print(f"Sum of dice numbers is {total}.")