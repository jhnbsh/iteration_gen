#!/usr/bin/python

#Program: iteration_gen v1.0
#Description
#     This python script generates all possible combinations of words from a provided
# dictionary for use in password cracking.  The input is a dictionary of words (see input.txt)
# and the output is a listing of all combinations based on the user supplied number of iterations. 
# Note: if too large a dictionary is used your computer will likely exhaust all RAM and this program will crash.

#Requried modules
import itertools

###START PROGRAM###

#User directions
print '\n Hello friend. The script is running. \n'
print 'How many iterations of words would you like to calculate?'
print 'ex: 2 = WordWord, 3 = WordWordWord, 4 = WordWordWordWord, etc. \n'
my_iterations = input("So, how many iterations? ")

#Open the dictionary and remove any whitespace
my_dictionary = list(open('input.txt', 'r'))
strip_dictionary = [elem.strip() for elem in my_dictionary]

#Create iterations
my_iterations = list(itertools.product(strip_dictionary, repeat=my_iterations))

#Write out results to a file without brackets or formatting
my_output = open('output.txt', 'w')
for item in my_iterations:
  my_output.write(('{}'*len(item)).format(*item) + '\n')
  
my_output.close() 

###END PROGRAM###
        
        