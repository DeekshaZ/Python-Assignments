'''-------------------------------------------------------------------------------------------------------
Name        :  Deeksha Surasani
Email       :  dsurasan@student.fitchburgstate.edu
Lab/Assg no :  Assignment 7
Description :  Program to print atomic mass of a given compound using the periodic table
----------------------------------------------------------------------------------------------------------'''
import csv
import time

'''
readTable() takes a file object as input and returns a dictionary where the key is the atomic symbol,
and the values are the name and the atomic mass of each element found in the CSV file separated by '/'.
'''
def readTable(fileObject) :
    reader = csv.reader(fileObject)
    elements = {}
    for row in reader:
        if(reader.line_num > 8):
            elements[row[1]] = row[5]+'/'+row[6]
    return elements

'''
parseElement() takes a string of the SymbolCount in such as ‘H2’, and return a tuple of the
form (Symbol, count) such as (‘H’, 2)
'''
def parseElement(elementString) :
    elementTuple = ()
    containsDigit = 0
    for i in range(0,len(elementString)) :
        if(elementString[i].isdigit()) :  #when a digit is found, create a tuple with values: substring before the digit,the remaining digits
            containsDigit = 1
            elementTuple = (elementString[0:i] , elementString[i:len(elementString)])
            break
    if(containsDigit == 0) : #when no digit is found, create tuple - (symbol , 1)
        elementTuple = (elementString , 1)
    return elementTuple
fileObj = open("Periodic_Table.csv", 'rU')
elementsDict = readTable(fileObj)
print("This program prints the atomic mass of a given compound using the periodic table")
compound = input("Input a chemical compound, hyphenated, eg., C-O2 : ")
compound = compound.split('-')  #List to hold the elements(including symbol counts) Eg., {C , O2}
atomicMass = 0
print("The compound is composed of : " , end = "")
for elementString in compound : #for each element in the compound list, parse it to create tuples and add the atomic mass
    elementTuple = parseElement(elementString)
    print(elementsDict[elementTuple[0]].split('/')[0] , end = " ")
    atomicMass = atomicMass + float(elementsDict[elementTuple[0]].split('/')[1]) * float(elementTuple[1])
print("\nThe atomic mass of the compound is : ",atomicMass)
time.sleep(5)
