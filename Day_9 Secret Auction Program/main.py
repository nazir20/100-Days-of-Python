def findWinner(bids):
    maxBid = 0
    winner = ""
    # bids = {"Egemen": 240, "Hakan": 136}
    for bidder in bids:
        bidAmount = bids[bidder]
        if bidAmount > maxBid:
            maxBid = bidAmount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${maxBid}")


from art import logo

print(logo)
bids = {}
isBidder = True

while isBidder:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        isBidder = False
        findWinner(bids)
