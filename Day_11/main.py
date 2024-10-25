# author @aesha98
# The Blackstone 21 Capstone Project

#Program requirement

#Goal of the game:
# add up the card to the largest number without going over 21
# if player card value is more than computer but not over 21 then player win
# if player card value is less than computer and not over 21 then player lose
# 

import os
import random

game_end = False
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player = []
dealer = []

# 
def clear():
	os.system('clear')

def calculate_score(users_card):
	total_score = 0
	for i in users_card:
		total_score = i
	return total_score

def draw_cards():
	for i in range(2):
		player.append(random.choices(cards))
	dealer.append(random.choice(cards))

def fetch_card():
	draw_cards()
	print(f"Your cards: {player} , current score: {calculate_score(player)}")
	print(f"Computer's first card: {calculate_score(dealer)}")
	get_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
	if get_card == 'y':
		fetch_card()
	elif get_card == 'n':
		final_score_player = calculate_score(player)
		final_score_cpu = calculate_score(dealer)
		print(f"Your final hands: {player} , final score: {final_score_player}")
		print(f"Computer's final hand: {dealer}, final score: {final_score_cpu}")

		# check winning condition

while not game_end:
	ask_user = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

	if ask_user == 'y':
		clear()
		fetch_card()
	elif ask_user == 'n':
		os._exit(0)


