import csv

file_data = []

def ReadFile():
    sample_file = open('sample.csv','r', newline='')
    sample_reader = csv.reader(sample_file)
    for row in sample_reader:
        for rowList in row:
            rowList = rowList.split(";")
            file_data.append(rowList)
            
    sample_file.close()

def printAgain():
    for i in range(len(file_data)):
        for j in range(len(file_data[i])):
            ele = file_data[i][j]
            ele = ele.ljust(15)
            print(ele, end="", flush=True)
        print('')

def InsertRow():
    print ("Please enter the student Infromation:")
    name = input('Name :')
    exam1 = input('Exam1 :')
    exam2 = input('Exam2 :')
    exam3 = input('Exam3 :')
    currentRowNum = len(file_data) - 1
    myString = 'Please enter the ROW number between [1, %d] to insert(if last row enter -1):' % currentRowNum
    rowNum = input(myString)
    rowNum = int(rowNum)
    newRow = [name, exam1, exam2, exam3]
    if rowNum < 1 or rowNum > currentRowNum:
        print("Adding the row to the end.")
        file_data.append(newRow)
    else:
        file_data.insert(rowNum, newRow)
    print("Data successfuly added, updated record:")    
    input('Please press ENTER to continue.')


def InsertColumn():
    title =  input('Please enter the title for the new column to add:')
    columnNum = len(file_data[0])
    myString = 'Please enter the COLUMN number between [2, %d] to insert(if last enter -1):' % columnNum
    usercolNum = input(myString)
    usercolNum = int(usercolNum)
    newMarks = []
    for i in range(1,len(file_data)):
        for j in range(1):
            ele = file_data[i][j]
            mystring = 'Please enter the %s for %s :' % (title, ele)
            mark = input (mystring)
            newMarks.append(mark)
   
    if usercolNum < 2 or usercolNum > columnNum:
        print("Adding the new column to the end")
        file_data[0].append(title)
        for i in range(1,len(file_data)):
            file_data[i].append(newMarks[i-1])
    else:
        usercolNum = usercolNum - 1
        file_data[0].insert(usercolNum, title)
        for i in range(1,len(file_data)):
            file_data[i].insert(usercolNum, newMarks[i-1])
    print("Data successfuly added, updated record:")    
    input('Please press ENTER to continue.')
   

def ChangeValueNew():
    record = input('Please enter the student name or the row number you wish to update: ')
    newvalues = []
    
    if record.isdigit():
        record = int(record)
        rowNum = len(file_data) - 1
        if int(record) > rowNum or int(record) < 1:
            print("Not a valid row number")
        else:
            print("The ROW you have choosen looks like:")
            count = 1
            for j in range(len(file_data[rowNum])):
                mystring = '(%d) %s : %s' % (count, file_data[0][j], file_data[record][j])
                print(mystring)
                count = count + 1
            columns = input('To update  the columns that you like please enter the number between ()  preceding the column shown above ?'
                      'For updating one column type the number to update ,more than one please enter number separated by comma (eg:1,3) :3'
                      'Enter the value with which you would like to replace  the selected columns:')
            columnList = columns.split(',')
            for i in columnList:
                ii = int(i)
                mystring = 'Please enter a new value for %s :' % file_data[0][ii-1]
                val = input(mystring)
                file_data[record][ii-1]=val
            
            print("Record successfully updated")
            
    else:
        index = -1
        for i in range(1, len(file_data)):
            if record.lower() == file_data[i][0].lower():
                index = i
        if index > 0:
            print("The ROW you have choosen looks like:")
            count = 1
            rowNum = len(file_data) - 1
            for j in range(len(file_data[rowNum])):
                mystring = '(%d) %s : %s' % (count, file_data[0][j], file_data[index][j])
                print(mystring)
                count = count + 1
            columns = input('To update  the columns that you like please enter the number between ()  preceding the column shown above ?'
                            'For updating one column type the number to update ,more than one please enter number separated by comma (eg:1,3) :3'
                            'Enter the value with which you would like to replace  the selected columns:')
            columnList = columns.split(',')
            for i in columnList:
                ii = int(i)
                mystring = 'Please enter a new value for %s :' % file_data[0][ii-1]
                val = input(mystring)
                file_data[index][ii-1]=val
            print("Record successfully updated")            
        else:
            print("No student with the given name exists")
    input('Please press ENTER to continue.')

def ChangeValue():
    record = input('Please enter the student name or the row number you wish to update: ')
    newvalues = []
    
    if record.isdigit():
        record = int(record)
        rowNum = len(file_data) - 1
        if int(record) > rowNum or int(record) < 1:
            print("Not a valid row number")
        else:
            for j in range(len(file_data[rowNum])):
                mystring = '%s :' % file_data[0][j]
                val = input(mystring)
                newvalues.append(val)
            file_data[record]=newvalues
            print("Record successfully updated")
            
    else:
        index = -1
        for i in range(1, len(file_data)):
            if record.lower() == file_data[i][0].lower():
                index = i
        if index > 0:
            rowNum = len(file_data) - 1
            for j in range(len(file_data[rowNum])):
                mystring = '%s :' % file_data[0][j]
                val = input(mystring)
                newvalues.append(val)
            file_data[index]=newvalues
            print("Record successfully updated")            
        else:
            print("No student with the given name exists")
    input('Please press ENTER to continue.')

def DeleteRow():
    record = input('Please enter the student name or the row number you wish to delete: ')
    if record.isdigit():
        record = int(record)
        rowNum = len(file_data) - 1
        if int(record) > rowNum or int(record) < 1:
            print("Not a valid row number")
        else:
            del file_data[record]
            print("Record successfully deleted")
           
    else:
        index = -1
        for i in range(1, len(file_data)):
            if record.lower() == file_data[i][0].lower():
                index = i
        if index > 0:
            rowNum = len(file_data) - 1
            del file_data[index]
            print("Record successfully deleted")            
        else:
            print("No student with the given name exists")
    input('Please press ENTER to continue.')

def DeleteColumn():
    columnNum = len(file_data[0])
    myString = 'Please enter the COLUMN number between [2, %d] to delete:' % columnNum
    usercolNum = input(myString)
    usercolNum = int(usercolNum)
    if usercolNum >= 2 and usercolNum <= columnNum:
        usercolNum = usercolNum - 1
        for i in range(0, len(file_data)):
            del file_data[i][usercolNum]
        print("Column successfully deleted.")        
    else:
        print("Not a valid ROW")
    input('Please press ENTER to continue.')


def OutputCSV():
    newfile = open('NewWorkbook.csv','w', newline='')           
    newwriter = csv.writer(newfile)
    for row in file_data:
        newwriter.writerow(row)
    newfile.close()
    print("The NewWorkbook.csv has been successfully created.")
    input('Please press ENTER to continue.')


def main():
    print ("This program helps you keep track of student scores, their average, and class average.")
    ReadFile()
    repeat = True
    while repeat:
        print()
        print ('--->>')
        print (" Please enter the numbrer below to select your option:")
        print (" '1' to PRINT the data")
        print (" '2' to DELETE a ROW")
        print (" '3' to DELETE a COLUMN")
        print (" '4' to INSERT a ROW")
        print (" '5' to INSERT a COLUMN")
        print (" '6' to CHANGE value in cell")
        print (" '7' to OUTPUT data in CSV format")
        print (" 'x' to EXIT")
        menu = input("\nPlease enter your choice now: ")
        if menu == '1':
            printAgain()
        elif menu == '2':
            DeleteRow()
        elif menu == '3':
            DeleteColumn()
        elif menu == '4':
            InsertRow()
        elif menu == '5':
            InsertColumn()
        elif menu == '6':
            ChangeValueNew()
        elif menu == '7':
            OutputCSV()
        elif menu == 'x':
            repeat = False
            print("Program Terminated.\n")
        else:
            print ("Invalid entry! Please try again.")

main()
'''
    k = len(data_list[0])
    for i in range(0,len(data_list)-1) :
        print(len(data_list[i])-1)
        for j in range(0,len(data_list[i])-1) :
            print("j : ",j)
            print("k : ",k)
            if(j >= k) :
                data_list[i][j] = ""
                print("herer :",data_list[i][j])
'''
