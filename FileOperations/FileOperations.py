'''-------------------------------------------------------------------------------------------------------
Name        :  Deeksha Surasani
Email       :  dsurasan@student.fitchburgstate.edu
Lab/Assg no :  Week 13
Description :  Program for CSV file operations
----------------------------------------------------------------------------------------------------------'''
import csv
data_list = list()
workbook_file  = open('sample.csv', 'r')
workbook_reader = csv.reader(workbook_file)
for row in workbook_reader:
    data_list.append(row)
workbook_file.close()

def printData() :
    for row in data_list:
        for entry in row :
            print(str(entry).ljust(15), end = '\t')
        print()
        
def writeFile(fileName) :
    workbook_file  = open(fileName, 'w' ,  newline = '')
    workbook_writer = csv.writer(workbook_file)
    for row in data_list :
        workbook_writer.writerow(row)
    workbook_file.close()
    
def deleteRow(key) :
    if key.isdigit() == True : #if row number is entered
        key = int(key)
        if key != 0 and key <= len(data_list)-3 :
            data_list.remove(data_list[key])
            print("ROW SUCCESSFULLY DELETED")
        else :
            print("INVALID ROW NUMBER")
    else : #if row name is entered
        found = 0
        for i in range(0,len(data_list)) :
            if data_list[i][0] == key :
                data_list.remove(data_list[i])
                print("ROW SUCCESSFULLY DELETED")
                found = 1
                break
        if(found == 0) :
            print("ROW NOT FOUND")

def deleteColumn(key) :
    if key.isdigit() == True : #if column number is entered
        key = int(key)
        if key != 0 and key <= len(data_list[0])-2 :
            for j in range(0,len(data_list[0])) :
                data_list[j].remove(data_list[j][key])
            data_list[len(data_list)-1].remove(data_list[len(data_list)-1][len(data_list[len(data_list)-1])-1])
            print("COLUMN SUCCESSFULLY DELETED")
        else :
            print("INVALID COLUMN NUMBER")
    else : #if column name is entered
        found = 0
        for i in range(0,len(data_list[0])) :
            if data_list[0][i] == key :
                found = 1
                #data_list[i].remove(data_list[i])
                break
        if(found == 1) :
            for j in range(0,len(data_list[0])) :
                data_list[j].remove(data_list[j][i])
            data_list[len(data_list)-1].remove(data_list[len(data_list)-1][len(data_list[len(data_list)-1])-1])
            print("COLUMN SUCCESSFULLY DELETED")
        else :
            if(found == 0) :
                print("COLUMN NOT FOUND")


def updateGradeAvg() :   #This function automatically updates grades and average
    colNum = len(data_list[0])-1
    average = 0
    if(colNum - 1 == 0) :
        data_list[1][colNum] = ""
        #data_list[len(data_list)-1][colNum] = ""
        return
    if(len(data_list)-3 == 0) :
        data_list[len(data_list)-1][colNum] = ""
        return
    for i in range(1,len(data_list)-2) :
        total = 0
        for j in range(1,colNum) :
            total = total + int(data_list[i][j])
        data_list[i][colNum] = round(float(total / (colNum - 1)),2)
        average = average + data_list[i][colNum]
    try :
        data_list[len(data_list)-1][colNum] = round(float(average/(len(data_list)-3)),2)
    except IndexError :
        return
    
choice = 1
while(choice in range(1,8)) :
    print("---------------------------------------------------------------------------")
    print("\nThis program helps you keep track of student scores their average and class average(CALCULATED AUTOMATICALLY)\nPlease enter the number between () to specify your option :\n(1)Print the data\n(2)Delete a row\n(3)Delete a column\n(4)Insert a row \n(5)Insert a column\n(6)Change value in cell\n(7)Output data in  csv format  :\nEnter your choice ,type something else to exit :")
    choice = int(input())
    
    if(choice == 1) :
        printData()
    elif(choice == 2):
        key = input("Please enter the student name or row number which you wish to delete : ")
        deleteRow(key)
        updateGradeAvg()
    elif(choice == 3):
        key = input("Please enter the column name or column number which you wish to delete : ")
        deleteColumn(key)
        updateGradeAvg()
    elif(choice == 4):
        print("Please enter the student information:")
        #read the data for each column
        newRow = list()
        for i in range(0,len(data_list[0])) :
            if(i != len(data_list[0])-1) :
                newRow.append(input(data_list[0][i]))
            else :
                newRow.append(0)
        #read the position where the row is to be inserted
        position = input("Please enter the row number to insert (if last row enter -1 other wise to insert in second row type 2)")
        position = int(position)
        if position != 0 and position >= 1 and position <= len(data_list)-3 :
            data_list.insert(position, newRow)
        else :
            data_list.insert(len(data_list)-2,newRow)
        updateGradeAvg()
    elif(choice == 5):
        colName = input("Please enter the title for the new student exam column to add :")
        newCol = list()
        newCol.append(colName)
        position = input("Please Enter the column number to insert your new exam column:")
        position = int(position)
        #read the data for each student
        print("Please enter the information for each student :")
        for i in range(1,len(data_list)-2) :
            newCol.append(input(data_list[i][0]))
        print(newCol)
        if position != 0 and position >= 1 and position <= len(data_list[0])-1 :
            for i in range(0,len(newCol)) :
                data_list[i].insert(position, newCol[i])
        else :
            for i in range(0,len(newCol)) :
                data_list[i].insert(len(data_list[0])-1,newCol[i])
        print(data_list)
        updateGradeAvg()        
        
    elif(choice == 6):
        record = input('Please enter the student name or the row number you wish to update: ')
        newvalues = []
        if record.isdigit():  #if row number is entered
            record = int(record)
            rowNum = len(data_list) - 1
            if record > rowNum - 2 or int(record) < 1:
                print("ROW NUMBER NOT VALID")
            else:
                print("The ROW you have choosen looks like:")
                count = 1
                for j in range(len(data_list[rowNum]) - 1):
                    mystring = '(%d) %s : %s' % (count, data_list[0][j], data_list[record][j])
                    print(mystring)
                    count = count + 1
                columns = input('To update  the columns that you like please enter the number between ()  preceding the column shown above'
                          'For updating one column type the number to update ,more than one please enter number separated by comma eg:1,3'
                          'Enter the value with which you would like to replace  the selected columns:')
                columnList = columns.split(',')
                for i in columnList:
                    j = int(i)
                    if(j > 0 and j < len(data_list[record])) :
                        mystring = 'Please enter a new value for %s :' % data_list[0][j-1]
                        val = input(mystring)
                        data_list[record][j-1]=val
                        print("Record successfully updated")
                    else :
                        print(i , " IS INVALID ENTRY")
                
                
        else: #if student name is entered
            index = -1
            for i in range(1, len(data_list)):
                if record.lower() == data_list[i][0].lower():
                    index = i
            if index > 0:
                print("The ROW you have choosen looks like:")
                count = 1
                rowNum = len(data_list) - 1
                for j in range(len(data_list[rowNum]) - 1):
                    mystring = '(%d) %s : %s' % (count, data_list[0][j], data_list[index][j])
                    print(mystring)
                    count = count + 1
                columns = input('To update  the columns that you like please enter the number between ()  preceding the column shown above'
                                'For updating one column type the number to update ,more than one please enter number separated by comma eg:1,3'
                                'Enter the value with which you would like to replace  the selected columns:')
                columnList = columns.split(',')
                for i in columnList:
                    j = int(i)
                    if(j > 0 and j < len(data_list[rowNum])) :
                        mystring = 'Please enter a new value for %s :' % data_list[0][j-1]
                        val = input(mystring)
                        data_list[rowNum][j-1]=val
                        print("Record successfully updated")
                    else :
                        print(i , " IS INVALID ENTRY")            
            else:
                print("No student with the given name exists")
        updateGradeAvg()
    elif(choice == 7):
        writeFile("ModifiedFile.csv")
        print("ModifiedFile.csv has been successfully created.")
