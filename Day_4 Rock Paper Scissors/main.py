# Write your code below this line 👇
from art import rock, paper, scissors
import random

ImageArr = [rock, paper, scissors]
try:
    userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper & 2 for Scissors: "))
    if userChoice > 2 or userChoice < 0:
        print("You've entered invalid number! You lose!")
    else:
        print("Your choice: ")
        print(ImageArr[userChoice])
        computerChoice = random.randint(0, len(ImageArr) - 1)
        print("Computer's choice: ")
        print(ImageArr[computerChoice])
        # comparing the user and computer's choice...

        if userChoice == computerChoice:
            print("Draw!")
        else:
            # user: rock ---- computer: paper
            if userChoice == 0 and computerChoice == 1:
                print("Computer Wins")
            # user: rock ---- computer: scissors
            elif userChoice == 0 and computerChoice == 2:
                print("You Win!")
            # user: paper ---- computer: rock
            elif userChoice == 1 and computerChoice == 0:
                print("You Win!")
            # user: paper ---- computer: scissors
            elif userChoice == 1 and computerChoice == 2:
                print("Computer Wins!")
            # user: scissors ---- computer: rock
            elif userChoice == 2 and computerChoice == 0:
                print("Computer Wins")
            # user: scissors ---- computer: paper
            else:
                print("You win!")
except:
    print("Some errors occurred")
