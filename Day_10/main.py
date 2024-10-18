# author aesha98
# Day 10: Calculator Program

from art import logo
import os

def clear():
	os.system('clear')

def subtract(first_num, second_num):
	total = first_num - second_num
	print(f"{first_num} - {second_num} : {total}")

def multiply(first_num, second_num):
	total = first_num * second_num
	print(f"{first_num} * {second_num} : {total}")

def add(first_num, second_num):
	total = first_num + second_num
	print(f"{first_num} + {second_num} : {total}")

def divide(first_num, second_num):
	total = first_num / second_num
	print(f"{first_num} / {second_num} : {total}")

def input_operation():
	operation = "+\n-\n*\n/\n"
	print(operation)
	opr = input("Pick an operation: ")
	return opr

def choose_operation(opr, first_num, second_num):
	if opr == '+':
		add(first_num, second_num)
	elif opr == '-':
		subtract(first_num, second_num)
	elif opr == '*':
		multiply(first_num, second_num)
	elif opr == '/':
		divide(first_num, second_num)

calculator_end = False

while not calculator_end:

	# print logo
	print(logo)
	first_num = input("what's the first number?: ")
	opr = input_operation()
	second_num = input("what's the second number?: ")
	

	# calculate input numbers
	choose_operation(opr, first_num=first_num, second_num=second_num)

	other = input(f"Type 'y' to continue with calculating with {second_num}, or type 'n' to start a new calculation: ").lower()

	# check condition
	if other == 'y':
		opr = input_operation()
		second_num = input("what's the second number?: ")
		choose_operation(opr=opr)
		other = input(f"Type 'y' to continue with calculating with {second_num}, or type 'n' to start a new calculation: ").lower()
	elif other == 'n':
		clear()

