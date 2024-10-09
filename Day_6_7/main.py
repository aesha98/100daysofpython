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

# display logo
print(hangman_art.logo)

for char in guess_word:
	word.append(char)

# game running
while(game):

	print("word to guess: " + guess_word)
	user_input_letter = input("Guess a letter: ").lower()

	# check answer
	for letter in word:
		if user_input_letter == letter:		
			word_to_fill.append(user_input_letter)
			print(word_to_fill)
			break
		elif lives == 0:
			game = 0
			break
		else:
			print(f"you guess {user_input_letter}. That's not in the word. You lose a life.")
			print(hangman_art.stages[lives - 1])
			print(f"************ You have {lives - 1}/6 lives left ************************")
			lives -= 1
			break