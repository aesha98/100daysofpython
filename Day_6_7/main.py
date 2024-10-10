# author @aesha98
# day 6 & 7 : The Hangman Game

import random
import hangman_words, hangman_art
import string

game = 1
guess_word = random.choice(hangman_words.list_words)
word_to_guess = guess_word.split()
word = []
word_to_fill = []
lives = 6
placeholder = ""

# display logo
print(hangman_art.logo)

for char in len(guess_word):
	placeholder += '_'
	word.append(char)

# game running
while(game):
	print("word to guess: " + placeholder)
	print(f"hint : {word}")
	user_input_letter = input("Guess a letter: ").lower()

	# check answer
	for letter in word:
		if user_input_letter == letter:		
			placeholder += letter
			break
	for letter in word:
		if user_input_letter != letter:
			placeholder += '_'
			break
	
	print(f"{''.join(placeholder)}")			
	
	if lives == 0:
		print(f"************ It was {guess_word}. Try again. ************************")
		game = 0
		break
	if user_input_letter != letter:
		print(f"you guess {user_input_letter}. That's not in the word. You lose a life")
		print(hangman_art.stages[lives - 1])
		print(f"************ You have {lives - 1}/6 lives left ************************")
		lives -= 1
	