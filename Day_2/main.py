# author @aesha98
# Day 2 : Tip Calculator

# Data types and manipulating strings

title = 'Welcome to tip calculator!\n'

# Display title
print(title)

# Fetch input - total bill
totalBill = float(input('What is the total bill?\n$'))

total = totalBill

# Fetch input - option tips
tip = float(input('How much tip would you like to give? 10, 12 or 15?\n'))

tip_as_percent = tip / 100

# calculate tip from bill amount
total *= tip_as_percent

# total overall bill including tip amount
total += totalBill

# Fetch input - total split
numOfPeople = int(input('How many people to split the bills?\n'))

# calculation
total_billed_tip = total / numOfPeople

# conver data type
totalConvert = str(round(total_billed_tip, 2))

# display output
print(f'Each person should pay: ${totalConvert}')