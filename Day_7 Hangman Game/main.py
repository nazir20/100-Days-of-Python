#
# @Hangman Game
#
from hangman_art import logo, stages
from hangman_words import word_list
import random

print(logo)
lives = 6  # lives variable is the amount of user's hearts
gameFinished = False
chosen_word = random.choice(word_list)  # picking up a random word from word_list
word_length = len(chosen_word)


print(f'Pssst, the solution is {chosen_word}.')  # Hint :)
display = []  # Create blanks
for _ in range(word_length):
    display += "_"

while not gameFinished:
    guess = input("Guess a letter: ").lower()
    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            gameFinished = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        gameFinished = True
        print("You win.")

    # Print the stages ( stages are imported from hangman_art.py module)
    print(stages[lives])
