import art
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

print(art.logo)

auction_finished = False
bids = {}
user_response = ""

while not auction_finished:

    name = input("What is your name?: ")

    bid = float(input("What is your bid?: $"))

    bids[name] = bid

    while (user_response != "yes" and user_response != "no"):

        user_response = input("Are there more bidders? Write 'yes' or 'no': ")

    if user_response == "no":
        auction_finished = True
    else:
        clear_console()
        user_response = ""

def calculate_highest_bidder():
    highest_bidder = bids[name]