#!/usr/bin/python

#The function that decides the a and b combination
def compare(a,b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1

#A while loop to run it three times
#Set the count variable to 0 and then run the loop
#Until the count varible reaches 3
#Grab two numbers from the user, store them in variables
#called num1 and num2. Then pass those to the function
#called compare. This will output the desired result
count = 0
while count < 3:
	num1 = int(input('Input first number '))
	num2 = int(input('Input second number '))
	user_output=compare(num1,num2)
	print (user_output)
	count = count + 1
