from replit import clear
#call clear() to clear the output in the console.

from art import logo
print(logo)

bidder_dictionary = {}
max_value = None
bidding_done = False

while not bidding_done:
  user_name = input("What is your name?\n")
  user_bid_price = input("What is your bet?\n$")

  bidder_dictionary[user_name] = user_bid_price

  is_other_bidder = input("Are there any other bidders? Type 'yes' if there are other bidders, otherwise type 'no'.\n")

  if is_other_bidder == "yes":
    clear()
  else:
    for bid in bidder_dictionary:
      bid_value = bidder_dictionary[bid]
      if max_value is None or bid_value > max_value:
        max_value = bid_value
        max_bidder = bid
    clear()
    print(f"The highest bidder is {max_bidder} with a final bid of ${max_value}.")
    bidding_done = True