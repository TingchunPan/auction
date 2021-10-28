

from art import logo
print(logo)

bid = {}
keepBid = True


def find_the_highest_bidder(bidder_record):
    high = 0
    winner = ""
    # bidder_record={"Wendy":123}
    for bidder in bidder_record:
        bid_amount = bidder_record[bidder]
    if bid_amount > high:
        high = bid_amount
        winner = bidder

    print(f"The highest is bidder is {winner}, \nand the bid is {high}")


while keepBid:
    name = input("What's your name? ")
    price = int(input("How much would you like to pay for the bid price? "))

    bid[name] = price
    new_user = input("Click 'yes'or 'no' to bid")
    if new_user == 'no':
        keepBid = False
        find_the_highest_bidder(bid)

    else:

        keepBid = True
