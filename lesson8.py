# Guess number

import random

secretNumber = random.randint(1,20)

for guessesTaken in range(1,7):
    print("Take a guess!")
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break

if guess == secretNumber:
    print("Good job! " + str(secretNumber))
else:
    print("Nope. it was " + str(secretNumber))
