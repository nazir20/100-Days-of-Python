#
# @Coffee Machine Python
#
# @imports
from coffeeResources import resources, MENU
from art import logo, turnOff


# @functions
# @defining a function which shows the Coffee Machine's current resource values.
# @param
# @totalMoney
def report(totalMoney):
    print("---- Current resources ----")
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${totalMoney}')


# @defining a function to check the resources if the coffee -
# machine has enough resources to make the user's order
# @param
# @order
# @return
def checkResources(order):
    orderIngredients = MENU[order]['ingredients']
    for item in orderIngredients:
        if orderIngredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink -
# should be deducted from the coffee machine resources
# @orderedCoffee
def deductIngredients(orderedCoffee):
    orderIngredients = MENU[orderedCoffee]['ingredients']
    for item in orderIngredients:
        resources[item] -= orderIngredients[item]


# @defining a function to process the coin user inserted
# quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
def processCoins():
    insertedMoney = 0
    print('Please insert coins!')
    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickles = int(input('How many nickles?: '))
    pennies = int(input('How many pennies?: '))
    insertedMoney = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return insertedMoney


# @param
# @money
# @coffeeName
# @coffeePrice
def makeCoffee(money, coffeeName, coffeePrice):
    inChangeMoney = round(money - coffeePrice, 2)
    print(f'Here is ${inChangeMoney} in change')
    print(f'Here is your {coffeeName}☕ Enjoy!')
    deductIngredients(coffeeName)


def coffeeMachine():
    turnMachineOff = False
    profit = 0
    print(logo)
    while not turnMachineOff:

        usersOrder = input('What would you like? (espresso/latte/cappuccino): ').lower()
        if usersOrder == 'report':
            report(profit)
        elif usersOrder == 'off':
            turnMachineOff = True
            print(turnOff)
            print("Machine is successfully turned off!")
        elif usersOrder == "espresso" or usersOrder == 'latte' or usersOrder == 'cappuccino':
            if checkResources(usersOrder):
                coffeePrice = MENU[usersOrder]['cost']
                totalInsertedMoney = processCoins()
                if totalInsertedMoney > coffeePrice:
                    makeCoffee(totalInsertedMoney, usersOrder, coffeePrice)
                    profit += coffeePrice
                else:
                    print('Sorry that is not enough money. Money refunded.')
        else:
            print("You've entered invalid inputs! Try again!")


coffeeMachine()
