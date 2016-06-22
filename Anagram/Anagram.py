'''-------------------------------------------------------------------------------------------------------
Name        :  Deeksha Surasani
Email       :  dsurasan@student.fitchburgstate.edu
Lab/Assg no :  Week 7
Description :  Program to check if the given words are anagrams
----------------------------------------------------------------------------------------------------------'''
import time
print("This program checks if the given words are anagrams.")
word = input("Enter two words separated by a space : ").split()
if(sorted(word[0].lower())==sorted(word[1].lower())): #sort the words and compare them
    print(word[0]," and ",word[1]," are anagrams")
else:
    print(word[0]," and ",word[1]," are not anagrams")
time.sleep(3)

