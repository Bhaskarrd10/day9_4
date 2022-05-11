from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)

bids = {}
bidding_finished = False

def find_heighest_bidder(bidding_record):
    heighest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > heighest_bid:
            heighest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with bid of ${heighest_bid}")

while not bidding_finished:
    name = input("what is your name ")
    price = input("what is your bid? $")
    bids[name] = price
    should_continue =input("Are there any other bidders? 'yes' or 'no'.")
    if should_continue == "no":
        bidding_finished = True
    elif should_continue == "yes":
        clear()