# author @aesha98
# caesar cipher program
import logo

def encode(message, shift_num):
	print("encode")

def decode(message, shift_num):
	print("decode")

print(logo.logo)

typeInput = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

# check type of input encryption
if (typeInput == 'encode'):
	message = input("Type your message:\n")
	shift_number = input("Type the shift number:\n")
	encode(message, shift_number)
elif (typeInput == 'decode'):
	message = input("Type your message:\n")
	shift_number = input("Type the shift number:\n")
	decode(message, shift_number)
