'''-------------------------------------------------------------------------------------------------------
Name        :  Deeksha Surasani
Email       :  dsurasan@student.fitchburgstate.edu
Lab/Assg no :  4
Description :  Program to implement Mastermind game
----------------------------------------------------------------------------------------------------------'''
import random
codeColors   =  "ABCDEF"
makersCode   =  "".join(random.sample("ABCDEF", 4))
history      =  ""
counter      =  1
breakersCode =  ""
print("********************MASTERMIND GAME********************\nThis is an implementation of MasterMind game. Here six different colors correspond to ABCDEF. A black peg is indicates a guess that is correct in both color and position.  A white peg indicates the existence of a correct color peg placed in the wrong position. Let's start!! ")
print("Please start guessing four alphabet at a time")

while(counter != 13):  #counter for the 12 rows
    breakersCode = input( "Guess " + str(counter) + " : " )
    
    if(not(breakersCode.isalpha())):   #check for the alphabet input
        print("Error : Wrong input! Code should be aphabet. Digits and special characters are not allowed")
        continue  #if input is other than alphabet , then prompt for the input again
    
    elif(len(breakersCode) != 4):  #check for the length of the code
        print("Error : Length of the code should be 4")
        continue

    for c in breakersCode:   #check for the Alphabet choosed(Should only choose between A to F)
        if(c not in "ABCDEFabcdef"):
            print("Error : You have to choose only between A to F")
            break

    if(c not in "ABCDEFabcdef"):  #if code not choosed using alphabet A to F, ask for the input again
        continue

    unique = "" 

    for c in breakersCode:  #check for duplicates in the code
        found = False
        if(c in unique):
            print("Error : Duplicates not allowed")
            found = True
            break
        unique = unique + c

    if(found == True):
        continue  # if duplicate found , prompt for the input again
    breakersCode = breakersCode.upper()  #change the input code to upper to allow both A to F and a to f

    if(breakersCode != makersCode):
        print("Incorrect!")
        counter      = counter + 1
        i  =  0
        blackpegs = 0
        whitepegs = 0
        while(i < 4):  #calculate black and white pegs
            if(breakersCode[i] == makersCode[i]):
                blackpegs = blackpegs + 1
            elif(breakersCode[i] in makersCode):
                whitepegs = whitepegs + 1
            i = i + 1
        print("Black pegs = ",blackpegs,"\nWhite pegs = ",whitepegs)
        history  =  history + "--------\nYour Guess " + str(counter-1) + " : " + breakersCode + "\nBlack Pegs : " + str(blackpegs) + "\nWhite Pegs : " + str(whitepegs) + "\n--------"
        # to keep track of the history of guesses
                
    else:
        print("!!!!!!!!!!!****YOU WON****!!!!!!!!!!!")
        break

if(counter == 13):
    print("****YOU LOST****")
print(makersCode + " is the correct code")
print("-----------------------------------\n"+history+"\n-----------------------------------")
