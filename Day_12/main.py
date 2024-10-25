from logo import logo
import random

def easy_attempt(anser):
	print("you have 10 guesses to guess the correct number")
	user_guess = input("make a guess: ")

def hard_attempt(answer):
	print("you have 5 guesses to guess the correct number")
	user_guess = input("make a guess: ")

game_end = False

while not game_end:

	print(logo)
	print("Welcome the number guesing game!")
	display = print("Im thinking of a number between 1 and 100\n")

	answer = random.randint(1, 100)

	diffculty = input("choose your difficulty. Type 'easy' or 'hard': ").lower()

	print(f"psst, the correct answer is {answer}")
	if diffculty == 'easy':
		easy_attempt(anser=answer)
	elif diffculty == 'hard':
		hard_attempt(answer=answer)
