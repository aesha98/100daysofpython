from art import logo
import os
# author @aesha98
# secret auction program

bid_dict = {}

def clear():
	os.system('clear')

def run_bid(name, bid):
	bid_dict[name] = bid
	
	highest_bid = 0
	name_winner = None

	for key_name,value_bid in bid_dict.items():
		if (value_bid > highest_bid):
			highest_bid = value_bid
			name_winner = key_name
			
	print(f"The winner is {name_winner} with bid of ${highest_bid}")
 
print(logo)
bid_end = False

while not bid_end:

	name = input("what is your name?: ").lower()
	bid = int(input("what is your bid?: $"))

	other = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

	if other == 'yes':
		clear()
		bid_dict[name] = bid
	elif other == 'no':
		run_bid(name=name, bid=bid)
		bid_end = True


