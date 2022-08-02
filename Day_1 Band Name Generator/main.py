#
# @Band Name Generator
#
if __name__ == '__main__':
    print("---- Welcome to the Band Name Generator! ----")
    # if you use Python version of lower than 3, use raw_input() function instead of input(). raw_input() function
    # reads a line from input (i.e. the cityName) and returns a string by stripping a trailing newline. raw_input()
    # was renamed to input() in Python version 3
    # I was using Python 2.7 version, and I used input() function to get inputs as string
    # It was giving me error, I was shocked! The very basic codes doesn't work 😅!
    cityName = input("Which city did you grew up in?: ")
    petName = input("What is the name of your pet?: ")
    bandName = cityName + " " + petName
    print("Your Band Name could be: " + bandName)
