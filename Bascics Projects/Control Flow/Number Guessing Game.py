###  Number Guessing Game (Control Flow)

import random

def guessing_game():
    number = random.randint(1, 10)
    while True:
        guess = int(input("Guess a number (1-10): "))
        if guess == number:
            print("Correct!")
            break
        else:
            print("Try again!")

guessing_game()