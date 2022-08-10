#
# @Blackjack game Python
#
import random
from art import logo


# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    """ @deal_card() function returns random cars from the cards list """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    newCard = random.choice(cards)
    return newCard


# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.
def calculate_score(card):
    """ calculate_score() function takes a list of cards and return the score calculated from the cards"""
    ace = 11
    # Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0
    # instead of the actual score. 0 will represent a blackjack in our game.
    if len(card) == 2 and sum(card) == 21:
        # 0 will represent a blackjack in our game.
        return 0
    # Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace
    # it with a 1. You might need to look up append() and remove().
    if ace in card and sum(card) > 21:
        card.remove(ace)
        card.append(1)

    return sum(card)


# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user
# both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user
# has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score
# is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "You lose! The computer has a Blackjack!"
    elif user_score == 0:
        return "You win! You have a Blackjack"
    elif user_score > 21:
        return "You lose! Your score is over 21!"
    elif computer_score > 21:
        return "You win! Computer's score is over 21!"
    elif computer_score > user_score:
        return "Computer Wins!"
    else:
        return "You win!"


def play_game():
    print(logo)
    # Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
    # user_cards = []
    # computer_cards = []
    global computer_score, user_score
    user_cards = []
    computer_cards = []
    is_game_over = False

    for i in range(2):
        """ @Dealing the user & computer 2 cards randomly using the deal_card() function """
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to
    # be repeated until the game ends.
    while not is_game_over:
        # Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is
        # over 21, then the game ends.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"User's cards: {user_cards} \tCurrent Score: {user_score}")
        print(f"Computer's cards: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the
            # deal_card( ) function to add another card to the user_cards List. If no, then the game has ended.
            deal_card_again = input("Type 'y' to get another card, type 'n' to pass: ")
            if deal_card_again == "n":
                is_game_over = True
            else:
                user_cards.append(deal_card())
    # Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing
    # cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game
# of blackjack and show the logo from art.py.
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
