'''-------------------------------------------------------------------------------------------------------
Name        :  Deeksha Surasani
Email       :  dsurasan@student.fitchburgstate.edu
Lab/Assg no :  Week 11
Description :  Program for breast cancer data classifier
----------------------------------------------------------------------------------------------------------'''
import time

def make_data_set(file_name): #This fuction creates a tuple for each line and returns a list of those tuples
    file = open(file_name,'r')
    data_set_list = list()
    for line in file :
        classifier = ""
        entry = line.strip().split(',') #strip the line of new line char
        if '?' not in entry:
            if(entry[10] == '2') :
                classifier = "b"
            else :
                classifier = "m"
            classifierTuple = (entry[0],classifier,int(entry[1]),int(entry[2]),int(entry[3]),int(entry[4]),int(entry[5]),int(entry[6]),int(entry[7]),int(entry[8]),int(entry[9]))
            data_set_list.append(classifierTuple)
    file.close()
    return data_set_list

def train_classifier(training_set_list):
    benign_avg = [0,0,0,0,0,0,0,0,0]
    malignant_avg = [0,0,0,0,0,0,0,0,0]
    total_avg = [0,0,0,0,0,0,0,0,0]
    benign_count = 0
    malignant_count = 0
    for patient in training_set_list:
        if(patient[1] == "b") :
            benign_count = benign_count + 1
            for i in range(0,9) :
                benign_avg[i] = patient[i+2]+benign_avg[i]  #sum of values of benign entry
        else :
            malignant_count = malignant_count + 1
            for i in range(0,9) :
                malignant_avg[i] = patient[i+2]+malignant_avg[i] #sum of values of malignant entry
    for i in range(0,9) : 
        benign_avg[i] = (float)(benign_avg[i]) / benign_count  #averages of benign entries
        malignant_avg[i] = (float)(malignant_avg[i]) / malignant_count  #averages of malignant entries
    for i in range(0,9) : 
        total_avg[i] = (float)(benign_avg[i] + malignant_avg[i])/ 2 #average of benign and malignant entries
    return total_avg

def classify_test_set_list(test_set_list, classifier_list):
    classifyList = []
    for entry in test_set_list :
        benign_count = 0
        malignant_count = 0
        for i in range(0,9) :
            if(entry[i+2] > classifier_list[i]) :
                malignant_count += 1
            else :
                benign_count += 1
        classifier = ""
        success = 0
        if(malignant_count > benign_count) :  #if malignant count > benign count, it is classified as malignant
            classifier = 'm'
        else :  #if benign count > malignant count, it is classified as benign
            classifier = 'b'
        if(entry[1] == classifier) :
            success = 1
        classifyList.append((entry[0],benign_count,malignant_count,classifier,success))
    return classifyList

def report_results(result_list):  #print the results
    success = 0
    for entry in result_list :
        if(entry[4] == 1) :
            success = success + 1
    print("Of ",len(result_list)," patients, there were ", len(result_list) - success," inaccuracies")

def main():
    print("Reading in training data...")
    training_file_name = "training_data.txt"
    training_set_list = make_data_set(training_file_name)
    #print(training_set_list)
    print("Done reading training data.\n")

    print("Training classifier..."    )
    classifier_list = train_classifier(training_set_list)
    #print(classifier_list)
    print("Done training classifier.\n")

    print("Reading in test data...")
    test_file_name = "fulltest_data.txt"
    test_set_list = make_data_set(test_file_name)
    #print(test_set_list)
    print("Done reading test data.\n")

    print("Classifying records...")
    result_list = classify_test_set_list(test_set_list, classifier_list)
    print("Done classifying.\n")

    report_results(result_list)

    print("Program finished.")

main()
time.sleep(4)
