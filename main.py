import art
import os

# Global variables declaration
auction_finished = False
bids = {}
user_response = ""

# Useful functions declaration
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate_highest_bidder():
    bids_list = bids.values()
    highest_bid = max(bids_list)
    highest_bidders = [] # There can be more than one highest bidder in case of a draw

    for key in bids:
        if bids[key] == highest_bid:
            highest_bidders.append(key)

    if len(highest_bidders) == 1:
        print(f"The winner is {highest_bidders[0]} with a bid of ${highest_bid}")
    else:
        print(f"The winners are {highest_bidders} with a bid of ${highest_bid}")

# Main execution block
print(art.logo)

while not auction_finished:

    name = input("What is your name?: ")

    bid = int(input("What is your bid?: $"))

    bids[name] = bid

    while (user_response != "yes" and user_response != "no"):

        user_response = input("Are there any other bidders? Type 'yes' or 'no': ")

    if user_response == "no":
        auction_finished = True
    else:
        clear_console()
        user_response = ""

calculate_highest_bidder()