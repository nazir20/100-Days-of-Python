# @Tip Calculator
if __name__ == '__main__':
    print("-- Welcome to the Tip Calculator! --")
    totalBill = float(input("What was the total bill?: $"))
    tipPercentage = int(input("What percentage tip would you like to give? 10, 12 or 15?: "))
    people = int(input("How many people to split the bill?: "))
    tipAmount = (totalBill * tipPercentage)/100
    finalBill = totalBill + tipAmount
    billPerPerson = round(finalBill/people, 2)
    print(f"Each person should pay ${billPerPerson}")
