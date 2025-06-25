from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)
print("Welcome to the secret auction program!")

auction_has_ended = False
bidders = {}

while not auction_has_ended:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  continue_auction = input("Are there any more players? (Y/N): ")

  auction_has_ended = continue_auction.lower() == "n"

  bidders[name] = bid
  clear()

max_bid = -1
winner = ""
for name in bidders:
  if bidders[name] > max_bid:
    max_bid = bidders[name]
    winner = name

print(f"The winner is {winner} with a bid of ${max_bid}!")