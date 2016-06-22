'''-------------------------------------------------------------------------------------------------------
Name        :  Deeksha Surasani
Email       :  dsurasan@student.fitchburgstate.edu
Lab/Assg no :  Week 6
Description :  Program to print the words containing vowels 'aeiou' in the same order:
----------------------------------------------------------------------------------------------------------'''
import time
def cleanWord(word): #to strip the carriage return
    word = word.strip().lower() 
    return word
def getVowelsInWord(word): #to get the vowels in the given word
    vowels = ''
    for char in word:
        if(char in "aeiou"):
            vowels = vowels + char
    return vowels

f = open('dictionary.txt', 'r')
lineCount = 0
print("Words containing vowels 'aeiou' in the same order:")
for line_str in f:
    word = cleanWord(line_str)
    if(len(word)>6):
        vowels = getVowelsInWord(word)
        if(vowels == 'aeiou'):
            print(word)
f.close()
time.sleep(5)
