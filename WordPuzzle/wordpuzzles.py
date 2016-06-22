'''-------------------------------------------------------------------------------------------------------
Name        :  Deeksha Surasani
Email       :  dsurasan@student.fitchburgstate.edu
Lab/Assg no :  Week 7
Description :  Word puzzle driver
----------------------------------------------------------------------------------------------------------'''
import time

# Assumes wordList.txt file of one word per line

def getWordList():
    ''' returns a list of words from a wordList.txt file '''
    dataFile = open("wordList.txt", "r")
    wordList = []   # start with an empty word list

    for word in dataFile : # for every word (line) in the file
            # strip off end-of-line characters and make each word lowercase
            # then append the word to the wordlist
        wordList.append(word.strip().lower())                     

    return wordList

def puzzle(wordList) :
    #1)	Find all uncapitalized, unhyphenated  word that contains all but one of the letters of the alphabet from “l” to “v” (“lmnopqrstuv”)

    print("---------------------------------------------------")
    print("1 - Words that contains all but one of the letters of the alphabet from “l” to “v”")
    for word in wordList:
        if(len(word) >= 10):
            alphaList = [] #List to keep track of which letters of "lmnopqrstuv" are present in the word
            for char in "lmnopqrstuv":
                if(char in word):
                    alphaList.append(char)
            if(len(alphaList) == 10): #if 10 letters of total 11 letters : "lmnopqrstuv" are present in the alphaList
                print(word)
                
    #2)	Find all uncapitalized, seven-letter words, where each word contains just a single vowel and does not have the letter ‘s’ anywhere within it.
                
    print("---------------------------------------------------")
    print("2 - Seven letter words where each word contains just a single vowel and does not have the letter 's' anywhere within it are")           
    for word in wordList:
        vowels = 0  #to keep track of vowels count. If its value is > 1, more than one vowel is present in the word 
        if(len(word) == 7 and 's' not in word):
            for char in "aeiou":
                if char in word :
                   vowels += 1
                   if word.count(char) > 1:  #to check if a single vowel is repeating in the word
                       vowels += 1
                       break
                if vowels > 1 :
                    break
            if vowels == 1 :
                print(word)


    #3)	The word mimeographs contains all the letters of memphisat least once.  Find other words that also contain all the letters of  memphisat

    print("---------------------------------------------------")
    print("3 - Other words that also contain all the letters of  memphisat")
    for word in wordList :
        found = True
        if len(word) >= 9 and word.count('m')>1 : #to check if the word length is >= 9 and letter 'm' occurs twice in the word
            for char in "memphisat" :
                if char not in word :
                    found = False   #if atleast one char in memphisat is not found in the word then found = False
            if(found == True) :
                print(word)

    #4)	Find all words that contain the string ‘tantan”

    print("---------------------------------------------------")
    print("4 - Words that contain the string tantan")
    for word in wordList :
        if "tantan" in word :
            print(word)

    #5)	The word marine consists of five consecutive, overlapping state postal abbreviations: Massachusetts (MA), Arkansas(AR), Rhode Isalnd(RI), Indiana(IN), and Nebraska(NE).  Find all seven letter words that have the same property.

    print("---------------------------------------------------")
    print("5 - seven letter words that have overlapping state postal abbreviations")
    postalAbbrList = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH',
                      'NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']
    for word in wordList :
        if len(word) == 7 : #seven letter words
            count = 0
            for i in range(0,6) : #7 letter words have 6 US state postal codes. For example, MALARIA = MA + AL + LA + AR + RI + IA
                if word.upper()[i:i+2] in postalAbbrList : #take two letters at a time and check if it is a US state abbr.
                    count += 1 # if the substring is a part of US state abbr, increase the counter
            if count == 6 : # if 6 abbrevations are found in that word, print word
                print(word)
               
    #6)	When you are writing a script, there are four letters of the alphabet that cannot be completed in one stroke: ‘i’ and ‘j’ (which require dots) and ‘t’ and ‘x’ (which require crosses).  Find all words that use each of these letters exactly once.

    print("---------------------------------------------------")
    print("6 - words that use each of i,j,t,x letters exactly once")
    for word in wordList :
        if word.count('i') == 1 and word.count('j') == 1 and word.count('t') == 1 and word.count('x') == 1:
            print(word)
    

    #7)	Find all words that contain the consecutive letters “nacl”.

    print("---------------------------------------------------")
    print("7 - words that contain the consecutive letters “nacl”")
    for word in wordList :
        if "nacl" in word :
            print(word)
                

    #8)	Find all words that contain the vowels a, e, i, o, and u in that order.

    print("---------------------------------------------------")
    print("8 - words that contain the vowels a, e, i, o, and u in that order")
    for word in wordList :
        vowelsPresent = ""
        if 'a' in word and 'e' in word and 'i' in word and 'o' in word and 'u' in word:
            if word.index("a") < word.index("e") < word.index("i") < word.index("o") < word.index("u"):
                print(word)
                
    

    #9)	Consider the word sure.  If I asked you to add two pairs of doubled letters to it to make an eight-letter word, you could add p’s and s’s to make suppress.  Find an eight-letter word resulting from adding two pairs of doubled letters to rate

    print("---------------------------------------------------")
    print("9 - Eight-letter word resulting from adding two pairs of doubled letters to rate")
    for word in wordList :
        newWord = word
        distinct = [] # this list will keep track of the letters which are two paired other than r,a,t,e
        if len(word) == 8 and word.count("r") == word.count("a") == word.count("t") == word.count("e") == 1 :
            for element in ['r','a','t','e']:
                newWord = newWord.replace(element,'') #extract letters in the word other than r,a,t,e
            for char in newWord :
                if char not in distinct :
                    distinct.append(char) # For the word maritime, distinct list will have ['m','i']
            if word.count(distinct[0]) == 2 and word.count(distinct[1]) == 2 : #check if each of the two letters in distinct list have occured twice in the word
                print(word," - Two letters which are doubled are : ",distinct)

    #10) Two U.S. state capitals have a prefix that is the name of the month.  Find them.
    
    print("---------------------------------------------------")
    print("10 - Two U.S. state capitals have a prefix that is the name of the month")
    monthList = ['january','february','march','april','may','june','july','august','september','october','november','december']
    capitalList = ['Montgomery','Juneau','Phoenix','Little Rock','Sacramento','Denver','Hartford','Dover','Tallahassee','Atlanta','Honolulu','Boise','Springfield',
                   'Indianapolis','Des Moines','Topeka','Frankfort','Baton Rouge','Augusta','Annapolis','Boston','Lansing','St. Paul','Jackson','Jefferson City',
                   'Helena','Lincoln','Carson City','Concord','Trenton','Santa Fe','Albany','Raleigh','Bismarck','Columbus','Oklahoma City','Salem','Harrisburg',
                   'Providence','Columbia','Pierre','Nashville','Austin','Salt Lake City','Montpelier','Richmond','Olympia','Charleston','Madison','Cheyenne']

    for month in monthList :
        for capital in capitalList :
            if capital.lower().startswith(month) :
                print(capital)

wordList = getWordList()
puzzle(wordList)
time.sleep(15)
