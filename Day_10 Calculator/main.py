# @calculator Python...
# @imports
from art import logo


#
# @functions
# @param
# @num1
# @num2
#
def add(num1, num2):
    """ ex: 2 + 2 = 4 """
    return num1 + num2


def subtract(num1, num2):
    """ ex: 12 - 4 = 8 """
    return num1 - num2


def multiply(num1, num2):
    """ ex: 7 * 8 = 56 """
    return num1 * num2


def divide(num1, num2):
    """ ex: 100 / 20 = 5 """
    return num1 / num2


# @operations dictionary includes the operation symbol as key & operation function name as value
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():

    print(logo)
    num1 = float(input("What's the first number?: "))
    for key in operations:
        print(key)
    calculationContinue = True

    while calculationContinue:
        operationSymbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        # @picking up the function name according to the user's selected operation from @operations dictionary
        calculate = operations[operationSymbol]
        answer = calculate(num1, num2)
        print(f"{num1} {operationSymbol} {num2} = {answer}")
        userContinue = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if userContinue == 'y':
            num1 = answer
        else:
            calculationContinue = False
            calculator()


calculator()
