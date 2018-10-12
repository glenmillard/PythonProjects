#!/usr/bin/python

#Python calculator - Glen M - 10 May 2017

#Create a function for each operation
def add_numbers(a, b):
	return a + b

def sub_numbers(a, b):
	return a - b

def mult_numbers(a, b):
	return a * b

def div_numbers(a, b):
	return a / b

#Take in the number as floating point, as we are not using the mod operator
#Error checking to make sure it's not a zero - I looked this up!
while True: 
	num1 = float(input('Enter your first number:'))
	if num1 <=0:
		print("No zeroes, only positive numbers")
		continue
	break

#Menu, kind of an RPN type of calculator
print('Enter your selection:')
print('1. add')
print('2. subtract')
print('3. multiply')
print('4. divide')

#Take the selection as a string, as it seems to not work properly unless I do so
selection = str(input('Your Choice?(1 / 2 / 3 / 4):'))

#Error checking to make sure it's not a zero - I looked this up!
while True: 
	num2 = float(input('Enter your second number:'))
	if num2 <= 0:
		print("No zeroes, only positive numbers")
		continue
	break

#Use an if/elif/else statement to do the operations - exit if the user entered an incorrect operand
if selection == '1':
	print (num1, "+", num2, "=",add_numbers(num1,num2))
elif selection == '2':
	print (num1, "-",num2, "=",sub_numbers(num1, num2))
elif selection == '3':
	print (num1, "*",num2, "=",mult_numbers(num1, num2))
elif selection == '4':
	print (num1, "/",num2, "=",div_numbers(num1,num2))
else:
	print("Hey, you didn't enter a proper choice - exiting now - try running it again!")
