# author @aesha98
# caesar cipher program
import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(message, shift, type):
	final_text = ""
	
	print(f"Here's the {type}d result : {final_text}")

print(logo.logo)

should_end = False

while not should_end:

	typeInput = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
	message = input("Type your message:\n")
	shift_number = int(input("Type the shift number:\n"))

	caeser(message=message,shift=shift_number, type=typeInput)

	restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n" )
	if (restart == 'no'):
		should_end = True
		print("Goodbye!")




