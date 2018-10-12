#!/usr/bin/python

#I added this for the time() functions. I wanted it to wait before printing lines.
import time

#Function to print three (3) lines
def three_lines():
	print("\n"),
	print("\n"),
	print("\n"),

#Function to print nine (9) lines
def nine_lines():
	three_lines()
	three_lines()
	three_lines()

#Function called clear_screen, but prints twenty-five (25) lines
#Use the function three_lines a total of eight (8) times and then add one newline, for a total of 25 lines
def clear_screen():
	three_lines()
	three_lines()
	three_lines()
	three_lines()
	three_lines()
	three_lines()
	three_lines()
	three_lines()
	print("\n"),

#Information to the screen
print("Now printing nine lines!")

#Execute the function nine_lines
time.sleep(1)
nine_lines()

#Information to the screen
print("Now, clearing the screen!")

#Execute the function to clear the screen
time.sleep(1)
clear_screen()
