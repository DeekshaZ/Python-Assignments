'''-------------------------------------------------------------------------------------------------------
Name        :  Deeksha Surasani
Email       :  dsurasan@student.fitchburgstate.edu
Lab/Assg no :  Week 9
Description :  Program to print word frequency in a file using dictionaries
----------------------------------------------------------------------------------------------------------'''
import time

def addWord(word , wordDict) :
    if word not in wordDict :
        wordDict[word] = 1  #if the word is not there in the dictionary, add the word and its value 1 to the dictionary
    else :
        wordDict[word] = wordDict[word] + 1  #if word is already in the dictionary, add 1 to its value

def processLine(line , wordDict) :
    wordList = []  # list of words: initialized to be empty
    words = line.replace("-","").replace(",","").replace(".","").strip().lower()
    wordList.extend(words.split()) # Extract words from the line into a list 
    for word in wordList : #iterate through the wordList
        addWord(word , wordDict)

def prettyPrint(wordDict): #print the unique word and its value(frequency)
    print("# of unique words in the file: " , len(wordDict))
    print("Word\t\tCount")
    print("-----------------------")
    for word in sorted(wordDict,key=wordDict.get,reverse = True):
        print("{:14s} {:3d}".format(word,wordDict[word]))
        
####################################################
wordCountDict = dict() #initialize empty dictionary
file = open('Ramayana.txt','r')
for line in file:
    processLine(line , wordCountDict)
file.close() #close the file
prettyPrint(wordCountDict)
time.sleep(8)

