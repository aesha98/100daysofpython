# author @aesha98
# caesar cipher program
import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']


def caeser(message, shift, type):
	final_text = ""
	if (type == 'decode'):
		shift *= -1
	for char in message:
		if char in alphabet:
			# grab index 
			position = alphabet.index(char)
			new_position = position + shift
			final_text += alphabet[new_position]
		if char in digits:
			position = digits.index(char)
			new_position
		else:
			final_text += char

	print(f"Here's the {type}d result : {final_text}")

print(logo.logo)

should_end = False

while not should_end:

	typeInput = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
	message = input("Type your message:\n")
	shift_number = int(input("Type the shift number:\n"))

	shift_number = shift_number % 25

	caeser(message=message,shift=shift_number, type=typeInput)

	restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n" )
	if (restart == 'no'):
		should_end = True
		print("Goodbye!")




