#
# @Higher Lower Game
#
# @imports
import random
from art import logo, vs
from game_data import data


# @functions
# @defining a function which fetches a random account from data list (imported from game_data.py)
def getRandomAccount():
    return random.choice(data)


# @defining a function which formats account's data into a printable format:
# ---- name * description * country ----
def formatAccountData(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f'{name}, a {description}, from {country}'


# @defining a function which checks the user guess : True || False
def checkUserGuess(userGuess, aFollowers, bFollowers):
    if aFollowers > bFollowers:
        return userGuess == 'a'
    else:
        return userGuess == 'b'


def game():
    score = 0
    gameContinue = True
    print(logo)
    accountA = getRandomAccount()
    accountB = getRandomAccount()
    while gameContinue:
        # @in case if both accounts are the same:
        while accountA == accountB:
            accountB = getRandomAccount()

        print(f'Compare A: {formatAccountData(accountA)}')
        print(vs)
        print(f'Against B: {formatAccountData(accountB)}')

        guess = input('Who has more followers? Type "A" or "B": ').lower()
        aFollowerCount = accountA['follower_count']
        bFollowerCount = accountB['follower_count']
        isCorrect = checkUserGuess(guess, aFollowerCount, bFollowerCount)  # True or False

        if isCorrect:
            score += 1
            print(f'You are right! Current score: {score}.')
            accountA = accountB
        else:
            gameContinue = False
            print(f'Sorry, that is wrong. Final score: {score}')


game()
