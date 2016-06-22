'''-------------------------------------------------------------------------------------------------------
Name        :  Deeksha Surasani
Email       :  dsurasan@student.fitchburgstate.edu
Lab/Assg no :  Week 6
Description :  Program to calculate poker hands probabilities
----------------------------------------------------------------------------------------------------------'''
import math
import time
print("This program calculates poker hand probabilities")
while(True):
    fileName = input("Please enter a file name : ")
    try :  #error checking if the file exists
        f = open(fileName, 'r')
        break
    except IOError :
        print("Error opening file : ",fileName)
lineCount = 0
twoPair = 0
onePair = 0
three = 0
straight = 0
flush = 0
fullHouse = 0
four = 0
straightFlush = 0
royalFlush = 0
nothing = 0

for line in f:
    list = line.strip().split(',')
    try : #error checking for the input conversion
        hand = int(list[10])  #convert the element at 10th index to int
    except (ValueError,IndexError):
        continue #if bad value is found, do not count, continue to the next line in the file
    lineCount += 1
    if(hand == 0):
        nothing += 1
    elif(hand == 1):
        onePair += 1
    elif(hand == 2):
        twoPair += 1
    elif(hand == 3):
        three += 1
    elif(hand == 4):
        straight += 1
    elif(hand == 5):
        flush += 1
    elif(hand == 6):
        fullHouse += 1
    elif(hand == 7):
        four += 1
    elif(hand == 8):
        straightFlush += 1
    elif(hand == 9):
        royalFlush += 1

print("Total hands in file   : ",lineCount)
print("Hand counts by rank number  : ",nothing, onePair, twoPair, three, straight, flush, fullHouse, four, straightFlush, royalFlush)
if(lineCount!=0):
    print("Probability : ")
    print("of nothing         : ",round((nothing/lineCount)*100,4),"%")
    print("of one pair        : ",round((onePair/lineCount)*100,4),"%")
    print("of two pair        : ",round((twoPair/lineCount)*100,4),"%")
    print("of three of a kind : ",round((three/lineCount)*100,4),"%")
    print("of a straight      : ",round((straight/lineCount)*100,4),"%")
    print("of a flush         : ",round((flush/lineCount)*100,4),"%")
    print("of a full House    : ",round((fullHouse/lineCount)*100,4),"%")
    print("of four of a kind  : ",round((four/lineCount)*100,4),"%")
    print("of a straight Flush: ",round((straightFlush/lineCount)*100,4),"%")
    print("of a royal Flush   : ",round((royalFlush/lineCount)*100,4),"%")
time.sleep(5)

