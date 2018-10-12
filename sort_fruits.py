#!/usr/bin/python

#Write out alphabetically sorted fruits from input file unsorted_fruits.txt
#function does as follows:
# create and input for a file
#creates and output for a file
def sort_fruits(infile, outfile):
    input = open(infile, 'r')
    output = open(outfile, 'w')
    unsorted = input.readlines()

#Steps through the file word by word
#sorts in alpha order    
    unsorted.sort()
    count = 0
    for i in unsorted:
        print ("Writing line %d") % count
        output.write(i)
        count += 1

#Shuts off the file handlers for the read and write    
    input.close()
    output.close()

#passes the name of the files to the function and infile, outfile - or unsorted and sorted        
if __name__ == '__main__':
    sort_fruits('new_unsorted_fruits.txt', 'sorted_fruits.txt')

i = 0
while i < 11:
	print ("using the while loop") 
	i += 1
