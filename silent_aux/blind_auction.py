#!/bin/python3
import os
from art import new_logo
# how to clear the screen on windows and nix
#os.system('cls' if os.name == 'nt' else 'clear')

bidders = {}

print(new_logo)
print("Welcome to the silent auction program.")

more_bidders = "yes"

while (more_bidders == "yes"):
    name = input("What is your name: ")
    bid = int(input("What is your bid: $"))
    bidders[name] = bid
    # breaks out of while if user types anything other than 'yes'
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    # clear the screen on nix or windows
    os.system('cls' if os.name == 'nt' else 'clear')

winner_name = ""
winner_bid = 0
for key in bidders:
    if bidders[key] > winner_bid:
        winner_name = key
        winner_bid = bidders[key]

print(f"The winner is {winner_name} with a bid of ${winner_bid}")
