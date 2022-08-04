#
# @Password Generator
#
#Password Generator Project
from art import logo
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print(logo)
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?: "))
nr_symbols = int(input(f"How many symbols would you like?: "))
nr_numbers = int(input(f"How many numbers would you like?: "))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""

for letter in range(0, nr_letters):
    password += random.choice(letters)
    # randomLetter = letters[random.randint(0, len(letters)-1)]
    # password += randomLetter
for symbol in range(0, nr_symbols):
    password += random.choice(symbols)
    # randomSymbol = symbols[random.randint(0, len(symbols)-1)]
    # password += randomSymbol
for number in range(0, nr_numbers):
    password += random.choice(numbers)
    # randomNumber = numbers[random.randint(0, len(numbers)-1)]
    # password += randomNumber

print(f"Your easy password: {password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# changing the password into a list in order to shuffle the characters inside the password
pwdList = list(password)
random.shuffle(pwdList)

newPassword = ""
for item in pwdList:
    newPassword += item
print(f"Your powerful password: {newPassword}")
