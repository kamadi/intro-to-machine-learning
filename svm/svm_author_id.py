#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
import sys
from time import time

sys.path.append("..\\tools\\")
from email_preprocess import preprocess
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

# features_train = features_train[:len(features_train) / 100]
# labels_train = labels_train[:len(labels_train) / 100]

clf = SVC(kernel='rbf', C=10000)

t0 = time()

clf.fit(features_train, labels_train)

print "training time:", round(time() - t0, 3), "s"

t1 = time()

prediction = clf.predict(features_test)

print "predicting time:", round(time() - t1, 3), "s"

accuracy = accuracy_score(prediction, labels_test)

print "accuracy:", accuracy

count = 0

for y in prediction:
    if y == 1:
        count += 1

print "Chris count:", count

#########################################################

# kernel="linear" accuracy:0.984072810011

# kernel="linear" small data set accuracy:0.884527872582

# kernel="rbf" accuracy: 0.616040955631

# kernel='rbf',C=10 accuracy: 0.616040955631
# kernel='rbf',C=100 accuracy: 0.616040955631
# kernel='rbf',C=1000 accuracy: 0.821387940842
# kernel='rbf',C=10000 accuracy: 0.892491467577
# kernel='rbf',C=10000 full data accuracy: 0.990898748578

# 10th -> 1,  26th -> 0, 50th -> 1

# Chris count 877
