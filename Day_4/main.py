# author @aesha98
# Day 4: Rock Paper Scissor Game

# IMPORTANT RULES:
# - Rock win against Scissors
# - Scissors win against Paper
# - Paper win against Rock

# randomisation and list
import random

#display program
user_input = int(input("What do you choose?:\n - 0 for Rock\n - 1 for Paper\n - 2 for Scissors.\n"))

# ascii representation
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock, paper, scissors]

computerInput = random.randint(0,2)

if((user_input == 0 and computerInput == 2) or (user_input == 1 and computerInput == 0) or (user_input == 2 and computerInput == 1)):
	print(game[user_input] + "\n")
	print(game[computerInput] + "\n")
	print("You Win")
elif(user_input == computerInput):
	print(game[user_input] + "\n")
	print(game[computerInput] + "\n")
	print("It's a tie")
else:
	print(game[user_input] + "\n")
	print(game[computerInput] + "\n")
	print("You lose. Game Over.")