'''-------------------------------------------------------------------------------------------------------
Name        :  Deeksha Surasani
Email       :  dsurasan@student.fitchburgstate.edu
Lab/Assg no :  Week 10
Description :  Program to compare two files using sets
----------------------------------------------------------------------------------------------------------'''
import time

def addWord(word , wordSet) :
    if len(word)>3 :#and word not in wordSet :
        wordSet.add(word)  #if the word is not there in the set, add the word

def processLine(line , wordSet) :
    wordList = []  # list of words: initialized to be empty
    words = line.replace("-","").replace(",","").replace(".","").replace(":","").replace(";","").strip().lower()
    wordList.extend(words.split()) # Extract words from the line into a list 
    for word in wordList : #iterate through the wordList
        addWord(word , wordSet)

def prettyPrint(wordSet1 , wordSet2): #print the unique word and its value(frequency)
    print("Count of unique words of length 4 or greater : ")
    print("Gettyburg Address : " , len(wordSet1) , ", Declaration of Independence : " , len(wordSet2))
    print("\nOperation\t\tCount")
    print("------------------------------")
    print("{:24s} {:3d}".format("Union",len(wordSet1 | wordSet2)))
    print("{:24s} {:3d}".format("Intersection",len(wordSet1 & wordSet2)))
    print("{:24s} {:3d}".format("Symmetric Difference",len(wordSet1 ^ wordSet2)))
    print("{:24s} {:3d}".format("GA-DoI",len(wordSet1 - wordSet2)))
    print("{:24s} {:3d}".format("DoI-GA",len(wordSet2 - wordSet1)))
    print("\nCommon Words to both\n------------------------------")
    sortedList = sorted(wordSet1 & wordSet2)
    counter = 0
    for word in sortedList:
        if counter == 4:
            counter = -1
            print("{:14s}".format(word))
        else:
            print("{:14s}".format(word) , end = " ")
        counter += 1
    print("\n------------------------------")
       
####################################################
print("This program compares words in two files: Gettyburg Address and DeclarationOfIndependence")
wordSet1 = set() #initialize empty dictionary
file = open('GettysburgAddress.txt','r')
for line in file:
    processLine(line , wordSet1)
file.close() #close the file
wordSet2 = set()
file = open('DeclarationOfIndependence.txt','r')
for line in file:
    processLine(line , wordSet2)
file.close() #close the file
prettyPrint(wordSet1 , wordSet2)
time.sleep(8)

