
questions = ("How old are you? ",
             "What's your favorite movie? ",
             "number of planets in solar system? ",
             "days in a month? ",
             "Days in a week? ")

options = ( ("A. 10", "B. 11", "C. 12", "D. 13"),
            ("A. Sholay", "B. War", "C. Avatar", "D. Dune"),
            ("A. 8", "B. 9", "C. 10", "D. 11"),
            ("A. 28", "B. 29", "C. 30", "D. 31"),
            ("A. 5", "B. 6", "C. 7", "D. 8"))

answers = ("A", "B", "C", "D", "D")
guesses = []

question_num=0
score = 0;

for question in questions:
    print("==============================")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, or D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        print("Correct!")
        print(f"You guessed the answer to question {answers[question_num]} is correct!")
        score += 1
    else:
        print(f"Sorry, You guessed the answer to question !{answers[question_num]} is incorrect!")
    question_num+=1

print(f"You answered correctly {score} times!")

print("------------------------------")
print("----------Result---------------")
print("------------------------------")

print("Answers: ")
for answer in answers:
    print(answer, end=" ")
print()
print("guesses: ")
for guess in guesses:
    print(guess, end=" ")

print()
print(f"your  score is {(score/ len(guesses)*100)}%")
