# author @aesha98
# day 6 & 7 : The Hangman Game

import random
import hangman_words, hangman_art
import string

game = 1
guess_word = random.choice(hangman_words.list_words)
word_to_guess = guess_word.split()
placeholder = []
lives = 6

# display logo
print(hangman_art.logo)

# blank guess
for _ in range(len(guess_word)):
	placeholder += '_'

# game running
while(game):

	print(f"word to guess: {' '.join(placeholder)}")
	user_input_letter = input("Guess a letter: ").lower()

	if user_input_letter in placeholder:
		print("You've already guess this")
		
	# check answer
	for index in range(len(guess_word)):
		letter = guess_word[index]

		if user_input_letter == letter:
			placeholder[index] = letter
	
	#check if user is wrong
	if user_input_letter not in guess_word:
		print(f"you guess {user_input_letter}. That's not in the word. You lose a life")
		print(hangman_art.stages[lives - 1])
		print(f"************ You have {lives - 1}/6 lives left ************************")
		lives -= 1
	
		if lives == 0:
			print(f"************ It was {guess_word}. Try again. ************************")
			game = 0
	
	# check if user win
	if '_' not in placeholder:
		game = 0
		print("You win")

	#print(f"{' '.join(placeholder)}")			
	
	