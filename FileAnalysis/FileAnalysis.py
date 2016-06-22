'''-------------------------------------------------------------------------------------------------------
Name        :  Deeksha Surasani
Email       :  dsurasan@student.fitchburgstate.edu
Lab/Assg no :  Week 7
Description :  Program to analyse file
----------------------------------------------------------------------------------------------------------'''
import time
## Gettysburg address analysis
# count words, unique words, common words

# http://showcase.netins.net/web/creative/lincoln/speeches/gettysburg.htm
# The speech from the above source is stored as a txt file in GettysburgAddress.txt
def makeWordList(gFile):
    ''' Create a list of words from the file '''
    wordList = []  # list of words: initialized to be empty
    for line in gFile:
        words = line.replace("-","").replace(",","").replace(".","").strip().lower()
        wordList.extend(words.split()) # Extract words from the line into a list 
    return wordList

def makeUnique(speech):
    ''' create a list of unique words '''
    unique = []    # list of unique words: initialized to be empty
    for word in speech:
        if(word not in unique):  # if word is not already in unique list, add word to unique list
            unique.append(word)
    return unique

###########################################################################
print("File Analysis: ")

gFile = open("GettysburgAddress.txt","r")
# 1. put words into a list
speechList = makeWordList(gFile)

# print the speech length
print("Speech Length : ",len(speechList))

# 2. make a list of unique words in speech
uniqueList = makeUnique(speechList)

# print the unique list and its length
print("Unique Length : ",len(uniqueList))
print(uniqueList)
time.sleep(5)
