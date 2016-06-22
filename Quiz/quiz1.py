'''
Name : Deeksha S
Email : dsurasan@student.fitchburgstate.edu
Quiz 1 : Program to find the two-digit number such that when you square it,
the resulting three-digit number has its rightmost two digits are the
same as the original two-digit number.
That is for a number in the form AB, AB * AB = CAB for some C
'''

for num in range(10,99):  #to loop through all 2 digit numbers
    square = num ** 2
    lastdigits = square%100
    if(num == lastdigits):
        print(num, " satisfies the form AB*AB=CAB.")
        print("Its square is: ",square)
