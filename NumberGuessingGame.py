import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Welcome to the Number Guessing Game!")
print(f"select a number between {lowest_num} and {highest_num}")
while is_running:
    guess = (input("Guess a number: "))

    if guess.isdigit():
        guess = int(guess)
        guesses+=1
        if guess<lowest_num or guess>highest_num:
            print(f"Invalid input, please enter numbers between {lowest_num} and {highest_num} only: ")
        elif guess < answer:
            print(f"Your guess is too low, try again")
        elif guess > answer:
            print(f"Your guess is too high, try again")
        else:
            print(f"You guessed the number {answer}: ")
            print(f"Number of guesses {guesses}!")
            is_running = False
            break
    else:
        print(f"Invalid input, please enter numbers only between {lowest_num} and {highest_num}: ")


