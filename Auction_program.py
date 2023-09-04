from Auction_art import logo
print(logo)

bids = {}
bidding_finished = False

def finding_winner(bidding_records):
    highest_bid = 0
    winner = ""
    for bidder in bidding_records:
        bid_amount = bidding_records[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")        

while not bidding_finished:
    name = input("What's your name: ")
    price = int(input("What's your price: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ")
    if should_continue == "no":
        bidding_finished = True
        finding_winner(bids)
