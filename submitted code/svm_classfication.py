# Written by Hui Soon Kim
"""
Description     : Implementing the SVM Classifier
"""

from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn import svm

import csv
import random
import timeit


if __name__ == "__main__":
    start = timeit.default_timer()
    reader1 = csv.reader(open("2011.csv"))
    reader2 = csv.reader(open("2012.csv"))
    reader1.next()
    reader2.next()
    #Attribute Name
    """
    ['School_Grade', 'Overall_ACH_Grade', 'Read_Ach_Grade', 'Math_Ach_Grade', 'Write_Ach_Grade', 
    'Sci_Ach_Grade', 'Overall_Weighted_Growth_Grade', 'Read_Growth_Grade', 'Math_Growth_Grade', 
    'Write_Growth_Grade', 'PCT_Black', 'PCT_hisp', 'PCT_White', 'PCT_FREE_MEAL', 'PCT_Single_Family', 
    'PCT_More_than_INCOME_60000', 'EDU_Population35to44years_Bachelorsdegreeorhigher', 
    'EDU_Population45to64years_Bachelorsdegreeorhigher']
    """
    
    # Load DataSet
    data_set = []
    for row in reader1:
        data_set.append(row) #2011 data
    for row in reader2:
        data_set.append(row) #2012 data
    #random.shuffle(data_set)
 
    # Separate Train(80%) and Test(20%)
    # Use all Direct Features such as 'Overall_ACH_Grade' and External Features such as 'PCT_Black'
    x_train_all_feature=[]
    x_test_all_feature=[]
    # Use Only External Features such as 'PCT_Black'
    x_train_only_ext_feature=[]
    x_test_only_ext_feature=[]
    # Y values
    y_train=[]
    y_test=[]
    num = 0
    for x in data_set:
        if num % 5 != 0:
            x_train_all_feature.append(x[1:])
            x_train_only_ext_feature.append(x[10:])
            y_train.append(x[0])
        else:
            x_test_all_feature.append(x[1:])
            x_test_only_ext_feature.append(x[10:])
            y_test.append(x[0])
        num += 1


    # Discritize the School Grade(if grade >= 10 "Good"=1, else "Bad"=0)
    for ii in xrange(len(y_train)):
        if int(y_train[ii]) >= 10:
            y_train[ii] = 1
        else:
            y_train[ii] = 0
    for ii in xrange(len(y_test)):
        if int(y_test[ii]) >= 10:
            y_test[ii] = 1
        else:
            y_test[ii] = 0

    #Model SVM Classfier Using all Internal and External Features
    clf = svm.SVC()
    clf.fit(x_train_all_feature, y_train)
    predictions = clf.predict(x_test_all_feature)
    print("\n1. SVM Result of Using ALL INTERNAL and EXTERNAL Features")
    print("----------------------------------------------------")
    print(" Number of Used Features: %d" % len(x_test_all_feature[0]))
    print(" Total Number of Data Objects: %d" % len(data_set))
    print(" Number of Training Objects: %d" % len(x_train_all_feature))
    print(" Number of Test Objects: %d" % len(x_test_all_feature))
    print(" Accuracy: %f" % accuracy_score(y_test, predictions))    

    #Model SVM Classfier Using Only External Features
    clf = svm.SVC(kernel='poly')
    clf.fit(x_train_only_ext_feature, y_train)
    predictions = clf.predict(x_test_only_ext_feature)
    print("\n2. SVM Result of Using ONLY EXTERNAL Features")
    print("----------------------------------------------------")
    print(" Number of Used Features: %d" % len(x_test_only_ext_feature[0]))
    print(" Total Number of Data Objects: %d" % len(data_set))
    print(" Number of Training Objects: %d" % len(x_train_only_ext_feature))
    print(" Number of Test Objects: %d" % len(x_test_only_ext_feature))
    print(" Accuracy: %f" % accuracy_score(y_test, predictions))    
    
    stop = timeit.default_timer()
    print("\n3. SVM Total Running Time")
    print("----------------------------------------------------")
    print(" %f seconds" % float(stop - start)) 
    