#Author: Jonathan Bankston
#KUID: 3097029
#Date: 2/16/23
#Lab: lab03
#Last modified: 2/17/23
#Purpose: This program counts a sequence that can either be case sensitve or not of a string

string = input('Enter a string: ')
case_sens = input('Would you like your string to be case sensitive (Y/y): ')
sequence = input('Enter a sequence you would like to count: ')

if case_sens.lower == 'y' or 'Y':
    count = string.count(sequence)
    
else:
    count = string.lower().count(sequence.lower())

print(f'Within the string {string} the sequence {sequence} appears {count} time(s)')

