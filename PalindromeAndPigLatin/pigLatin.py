'''
Name  : Deeksha S
Email : dsurasan@student.fitchburgstate.edu
Week  : 5
Desc  : Program to take a string as input and convert it to PigLatin
'''
vowels = "aeiouAEIOU"
while(True):
    inputString = input("Please enter an English word to be translated into PigLatin(You can enter . to exit) : ")
    if(inputString == "."):  #exit the program if uses inputs period
        break
    elif(inputString[0] in vowels):
        modifiedString = inputString+"yay"  #if input string starts with a vowel
    else:
        for vowel in vowels:
            i = inputString.find(vowel)
            if(i >= 0):
                break
        if(i>=0):
            modifiedString = inputString[i::]+inputString[0:i]+"ay"  #if a vowel is found
        else:
            modifiedString = inputString+"ay"  #if no vowels are found
    print(inputString , "in PigLatin is : ",modifiedString)
