'''-------------------------------------------------------------------------------------------------------
Name        :  Deeksha Surasani
Email       :  dsurasan@student.fitchburgstate.edu
Lab/Assg no :  Week 8
Description :  Program to print max and min mileage cars from the data in the given  EPA file
----------------------------------------------------------------------------------------------------------'''
import time
def createMileageList(f):
    mileageList = []
    f.seek(0)
    f.readline() #to skip first line
    for line in f:
        if(("VAN" not in line) and ("PICKUP" not in line)): #skip lines with VAN and PICKUP
            l = line.split(',')
            car = (int(l[9]),l[1],l[2])  #create tuple
            mileageList.append(car)
    return mileageList
inputFile = open('epaData_2008.csv','r')
#Part 1 code
'''
print("There are ",len(inputFile.readline().split(','))," fields in the file.\nHere are the lines with FERRARI in them:\n")
for line in inputFile:
    if "FERRARI" in line:
        print(line[:75])
'''
mileageList = createMileageList(inputFile)
maxMileage = max(mileageList)[0] #get maximum mileage
minMileage = min(mileageList)[0] #get minimum mileage
print("EPA car mileage")
print("Maximum and Minimum mileage : ",maxMileage, minMileage)
maxMileageList = []
minMileageList = []
for car in mileageList:
    if(car[0] == maxMileage):
        maxMileageList.append(car[1]+" "+car[2])  #if a car has max mileage add make and model in maxMileageList
    elif(car[0] == minMileage):
        minMileageList.append(car[1]+" "+car[2])  #if a car has min mileage add make and model in minMileageList
print("\nMaximum mileage cars :\n")
for car in maxMileageList:
    print(car)
print("\nMinimum mileage cars :\n")
for car in minMileageList:
    print(car)
time.sleep(4)
