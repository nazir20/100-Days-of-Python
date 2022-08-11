#
# @Number Guessing Game @Python
#
# @imports
import random
from art import logo

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5


# @defining a functions which returns a random number between 1 & 100
def getRandomNumber():
    randomNumber = random.randint(1, 101)
    return randomNumber


# @defining a function to set the game's difficulty according to the user's choice :)
def setDifficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = getRandomNumber()
    print(f"Pssst, the correct answer is {number}")
    attempts = setDifficulty()
    make_a_guess = True
    while make_a_guess:
        userGuess = int(input("Make a guess: "))
        if userGuess == number:
            make_a_guess = False
            print(f"You got it! The answer is {number}")
        else:
            if userGuess > number:
                attempts -= 1
                print("Too high!")
            else:
                attempts -= 1
                print("Too low!")

            if attempts < 1:
                make_a_guess = False
                print(f"No more attempts! You lose! The answer was {number}")
            else:
                print("Guess again!")
                print(f"You have {attempts} attempts remaining to guess the number.")


game()
