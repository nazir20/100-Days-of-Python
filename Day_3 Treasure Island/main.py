#
# @Treasure Island Game
#
from art import logo, gameOver, win

print(logo)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
playerChoice1 = input("You're at a cross road. Where do you want to go? Type 'left' or 'right': ").lower()
if playerChoice1 == "right":
    print(gameOver)
    print("You fell into a hole!")
else:
    print("You've come to a lake. There is an island in the middle of the lake.")
    playerChoice2 = input("Type 'wait' to wait for a boat, type 'swim' to swim across: ").lower()
    if playerChoice2 == "swim":
        print(gameOver)
        print("You got attacked by an angry trout.")
    else:
        print("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.")
        playerChoice3 = input("Which color do you choose: ").lower()
        if playerChoice3 == "red":
            print(gameOver)
            print("It is a room full of fire!")
        elif playerChoice3 == "blue":
            print(gameOver)
            print("You enter a room of beasts!")
        elif playerChoice3 == "yellow":
            print(win)
            print("You found the treasure!")

        else:
            print(gameOver)
            print("You choose a door that doesn't exist!")



