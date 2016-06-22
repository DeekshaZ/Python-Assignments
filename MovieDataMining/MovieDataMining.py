'''-------------------------------------------------------------------------------------------------------
Name        :  Deeksha Surasani
Email       :  dsurasan@student.fitchburgstate.edu
Lab/Assg no :  Assignment 8
Description :  Program for Datamining imdb data
----------------------------------------------------------------------------------------------------------'''
import time
def createDictionary ( file ) :  #funtion to create movies dictionary with keys as the Movie Names and the value as the set of actors
    moviesDictionary = dict()
    for line in file :
        lineList = line.strip('\n').split(',')
        for i in range(1,len(lineList)):
            actorSet = set()
            if(lineList[i] not in moviesDictionary) :
                actorSet.add(lineList[0])
                moviesDictionary[lineList[i]] = actorSet
            else :
                moviesDictionary[lineList[i]].add(lineList[0])
    return(moviesDictionary)

def printActors ( moviesDictionary , movie1 , movie2 , operation ) : #function to print actors according to given operation
    movie1 = " "+movie1
    movie2 = " "+movie2
    if(operation == '|') :
        print("All the actors in those movies : ", moviesDictionary[movie1]| moviesDictionary[movie2])
    elif(operation == '&') :
        if(len(moviesDictionary[movie1] & moviesDictionary[movie2]) == 0) : #if there are no common actors, print NONE
            print("The common actors in the two movies : NONE")
        else :
            print("The common actors in the two movies : ", moviesDictionary[movie1] & moviesDictionary[movie2])
    elif(operation == '-') :
        if(len(moviesDictionary[movie1] ^ moviesDictionary[movie2]) == 0) :
            print("The actors who are in either of the movies but not both : NONE")
        else :
            print("The actors who are in either of the movies but not both : ", moviesDictionary[movie1] ^ moviesDictionary[movie2])

def printCoActors ( moviesDictionary , actor ) : #function to print co-actors of an actor
    coactorsSet = set()
    for key in moviesDictionary :
          if(actor in moviesDictionary[key]) :
             coactorsSet = coactorsSet | moviesDictionary[key]
    coactorsSet = coactorsSet - {actor}
    if(len(coactorsSet) != 0) :
        print("The actors with whom he/she has acted : ")
        for actor in coactorsSet :
            print(actor , end = "   ")
    else :
        print("The actors with whom he/she has acted : None")
    print()

##########################################################
        
file = open('imdb_Data.txt','r')
moviesDictionary = createDictionary(file)
print("This program gives the information of the actors in the given movies and their co-actors")
inputName = '1'
while(inputName != '0') :
    print("---------------------------------------------------")
    print("Enter the name of the two movies seperated by appropriate operator : '|' for all actors, '&' for finding common actors, '-' for actors who are in either of the movies but not both. For example, 'Meet Joe Black (1998)&Mr & Mrs. Smith(2005)', WITHOUT SPACES before and after the operation")
    print("(or) Enter actor's name to find his/her co-actors")
    print("Press 0 to exit")
    inputName = input()
    inputLength = len(inputName)
    i = 0
    findMovie = False
    try:
        while(i < inputLength and inputName[i] != ')') : #traverse until ')' is found
            i = i + 1
        if(i != inputLength) :
            operation = inputName[i+1]
            if(operation == '&' or operation == '|' or operation == '-') :
                movie1 = inputName[0:i+1]
                movie2 = inputName[i+2:inputLength]
                printActors( moviesDictionary , movie1 , movie2 , operation)
                findMovie = True
        if (findMovie == False) :
            printCoActors( moviesDictionary , inputName )
    except:
        IndexError
        ValueError
print("Exiting the program....")
time.sleep(2)
