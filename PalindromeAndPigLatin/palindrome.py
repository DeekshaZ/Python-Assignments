'''
Name  : Deeksha S
Email : dsurasan@student.fitchburgstate.edu
Week  : 5
Desc  : Palindrome tester
'''
import string

originalStr = input('This program checks for a palindrome. Please Input a string: ')
lowerStr = originalStr.lower()
modifiedStr = ""

bad_chars = string.whitespace + string.punctuation

for char in lowerStr:
    if char not in bad_chars: # remove bad characters
        modifiedStr = modifiedStr+char

if(modifiedStr == modifiedStr[::-1]): #it is a palindrome
    print(\
    'The original string is: {}\n\
     The modified string is: {}\n\
     The reversal is: {}\n\
     String is a palindrome'. format(originalStr, modifiedStr, modifiedStr[::-1]))
else:
    print(\
    'The original string is: {}\n\
     The modified string is: {}\n\
     The reversal is: {}\n\
     String is not a palindrome'. format(originalStr, modifiedStr, modifiedStr[::-1]))
