# author @aesha98
# PyPassword Generator

import random

# display program
print("Welcome to PyPassword Generator\n")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z','A','B', 'C' , 'D', 'E', 'F', 'G', 'H', 'I' ,'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S' ,'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['!','@','#','$','%','^', '&', '*', '(' ,')', '_', '+']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# user input
np_letter = int(input("How many letter would like in your password?\n"))

np_symbols = int(input("How many symbol would you like in your password?\n"))

np_number = int(input("How many numbers would you like in your password?\n"))

passwd = []

# loop
for char in range(1, np_letter + 1):
	passwd.append(random.choice(letters))

for symb in range(1, np_symbols + 1):
	passwd.append(random.choice(symbols))

for num in range(1, np_number + 1):
	passwd.append(random.choice(numbers))

print(passwd)
password = ''.join(random.choice(passwd) for i in range(len(passwd) ))

# output 
print(f"Your password is : {password}")
