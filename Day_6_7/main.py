# author @aesha98
# day 6 & 7 : The Hangman Game

import random
import hangman_words, hangman_art

# TEST: print random words
game = 1
guess_word = random.choice(hangman_words.list_words)
word_to_guess = guess_word.split()
word = []
word_to_fill = []

# display logo
print(hangman_art.logo)

# game running
while(game):

	print("word to guess: " + guess_word)
	user_input_letter = input("Guess a letter: ").lower()

	# push char into new list
	for char in guess_word:
		word.append(char)
	
	# check answer
	for letter in word:
		if letter == user_input_letter:		
			word_to_fill.append(user_input_letter)
			print(word_to_fill)
			break


