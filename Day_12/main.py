from logo import logo
import random
import os

game_end = False

def easy_attempt(anser, attempt):
	print(f"you have {attempt} guesses to guess the correct number")
	user_guess = int(input("make a guess: "))
	
	while attempt != 0:
		if user_guess > anser:
			print("Too High\nGuess Again")
			attempt -= 1
			easy_attempt(anser=anser,attempt=attempt)
		elif user_guess < anser:
			print("Too Low\nGuess Again")
			attempt -= 1
			easy_attempt(anser=anser,attempt=attempt)
		elif user_guess == anser:
			print("You win!")
			os._exit(0)
	print('You are out of guesses. You Lose! :(')
	game_end = True
	os._exit(0)


def hard_attempt(answer, attempt):
	print(f"you have {attempt} guesses to guess the correct number")
	user_guess = int(input("make a guess: "))

	while attempt != 1:
		if user_guess > answer:
			print("Too High\nGuess Again")
			attempt -= 1
			easy_attempt(anser=answer,attempt=attempt)
		elif user_guess < anser:
			print("Too Low\nGuess Again")
			attempt -= 1
			easy_attempt(anser=answer,attempt=attempt)
		elif user_guess == answer:
			print("You win!")
			os._exit(0)
	print("You are out of gueeses. You Lose! :(")
	game_end = True
	os._exit(0)


while not game_end:

	print(logo)
	print("Welcome the number guesing game!")
	display = print("Im thinking of a number between 1 and 100\n")

	answer = random.randint(1, 100)

	diffculty = input("choose your difficulty. Type 'easy' or 'hard': ").lower()

	print(f"psst, the correct answer is {answer}")
	if diffculty == 'easy':
		easy_attempt(anser=answer, attempt=10)
	elif diffculty == 'hard':
		hard_attempt(answer=answer, attempt=5)
