# author aesha98
# Day 10: Calculator Program

from art import logo
import os

def clear():
	os.system('clear')

def subtract():
	print("-")

def multiply():
	print("*")

def add():
	print("+")

def divide():
	print("/")

def input_operation():
	operation = "+\n-\n*\n/\n"
	print(operation)
	opr = input("Pick an operation:")
	return opr

calculator_end = False

while not calculator_end:

	# print logo
	print(logo)
	first_num = input("what's the first number?: ")
	opr = input_operation()
	second_num = input("what's the second number?: ")
	other = input(f"Type 'y' to continue with calculating with {second_num}, or type 'n' to start a new calculation: ").lower()

	if other == 'y':
		clear()
	elif other == 'n':
		clear()
		
