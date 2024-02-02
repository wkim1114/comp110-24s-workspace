"""Number guessing game."""

from random import randint

SECRET: int = randint(1, 100)
correct: bool = False

while not correct: # correct == False
    guess: int = int(input("Guess a number: "))
    if guess == SECRET:
        print(f"You got it right! {guess} is the secret number!")
        correct = True
    else: 
        if guess > SECRET:
            print("Try again! Too high!")
        else:
            print("Try again! Too low!")