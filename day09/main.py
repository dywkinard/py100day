import os
from art import logo
#HINT: You can call clear() to clear the output in the console.
highest_bid = -1
winner = None
bidders = dict()
print(logo)

while True: 
  name = input("What is your Name? ")
  bid = int(input("What is your bid? $"))
  bidders[name] = bid
  bid_continue = input("Are there any other bidders? 'yes' or 'no\n")

  if bid_continue == "no":
    for person,bid in bidders.items():
      if bid > highest_bid:
        highest_bid = bid
        winner = person
    break
  else:
    os.system('cls' if os.name == 'nt' else 'clear')
print(f"The winner is {winner} with a bid of ${highest_bid}!")