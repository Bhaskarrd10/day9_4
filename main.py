from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)

bids = {}
bidding_finished = False
while not bidding_finished:
    name = input("what is your name ")
    price = input("what is your bid? $")
    bids[name] = price
    shoud_continue =input("Are there any other bidders? 'yes' or 'no'.")
    if shoud_continue == "no":
        bidding_finished = True