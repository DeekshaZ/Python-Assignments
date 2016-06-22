'''-------------------------------------------------------------------------------------------------------
Name        :  Deeksha Surasani
Email       :  dsurasan@student.fitchburgstate.edu
Lab/Assg no :  Assignment 6
Description :  Data mining of Google's stock
----------------------------------------------------------------------------------------------------------'''
def getDataList (filename):
    dataFile = open (filename, 'r')
    dataList = [ ]  # start with an empty list
    dataFile.readline()
    for line in dataFile:  # read one line at a time from the dataFile
        l = line.strip('\n').split(',') #strip end-of-line, split on commas, and append items to list. 
        dataList.append(l)
    dataFile.close() #close the file
    return dataList

def getMonthlyAverages (dataList):
    monthlyAvgList = [ ] #list of the stock's monthly averages and their corresponding dates
    date = dataList[0][0].split('/')[0]+"/"+dataList[0][0].split('/')[2]
    avgPrice = 0
    totalVol = 0
    price = 0
    length = len(dataList)
    for i in range(0,length) :
        element = dataList[i]
        date1 = element[0].split('/')[0]+"/"+element[0].split('/')[2] #split the date and consider the month and the year
        if(date1 == date) :
            price = price + (float(element[5]) * float(element[6])) #calculate total price
            totalVol = totalVol + float(element[5]) #calculate total vol
        else :
            avgPrice = price / totalVol #calculate average price
            monthlyavg = (date , avgPrice)
            monthlyAvgList.append(monthlyavg)
            date = date1
            avgPrice = 0
            totalVol = 0
            price = 0
    return monthlyAvgList

def print_Info (monthlyAveragesList):
    monthlyAveragesList = sorted(monthlyAveragesList,key=lambda x: x[1])
    monthlyAveragesList.reverse()
    print("6 best and worst average price for google stock: ") 
    for i in range(0,6):
        print(monthlyAveragesList[i][0]+' , '+str(monthlyAveragesList[i][1]))
        print(monthlyAveragesList[-i][0]+' , '+str(monthlyAveragesList[-i][1])) 
         
dataList = getDataList('GoogleStockPrices.csv')
monthlyAvgList = getMonthlyAverages(dataList)
print_Info(monthlyAvgList)

