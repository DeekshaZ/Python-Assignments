'''
Name : Deeksha S
Email : dsurasan@student.fitchburgstate.edu
Quiz 1 : Program to convert hexadecimal integer to decimal
'''
choice = 'y'
while(choice == 'y' or choice == 'Y'):
    hexValue = input("Enter a valid hexadecimal number: ")
    #we can use int(hexValue,0) where hexValue = "0x"+hexValue
    hexString=hexValue.upper()
    hexDigits = "0123456789ABCDEF"
    dec = 0 #intialize decimal value to 0
    for i in range(0,len(hexString)): #loop through 0 to length of input string
            c = hexString[i]; #get the char
            ind = hexDigits.index(c) #find the position of that char in the hexDigits string which gives the decimal number corresponding to that hexadecimal char
            dec = 16*dec + ind  #if ABC is input, dec = 10 * 16**2 + 11 * 16**1 + 12 * 16*0 
    print(hexValue," converted to decimal is: ",dec)
    choice = input("Do you want to try again? Enter Y or N : ")
print("Good bye!")

