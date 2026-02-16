import random

options = ("rock", "paper", "scissors")
is_running = True

while is_running:
    Player = None
    Computer = random.choice(options)

    while Player not in options:
        Player = input("Enter a choice (Rock, Paper, Scissors): ")

    if Player == Computer:
        print("Draw!")
    elif Player == "rock" and Computer == "scissors":
        print("You win!")
    elif Player == "paper" and Computer == "rock":
        print("You win!")
    elif Player == "scissors" and Computer == "paper":
        print("You win!")
    else:
        print("You lose!")
    print(f"Player: {Player}, Computer: {Computer}")
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        is_running = False


print("Game Over!")





