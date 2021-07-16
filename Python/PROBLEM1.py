#!/usr/bin/env python
# coding: utf-8

# In[14]:


#Name:                   Nikita Singh
#Roll Number:            20075060
#Branch and section:     CSE Btech BA1
#Email:                  nikita.singh.cse20@itbhu.ac.in

                                     #PROBLEM 1
    
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split    
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
import seaborn as sns
sns.set_style("darkgrid")


df=pd.read_csv('Problem1.txt',delimiter='\t')
print(df['fruit_name'].unique())
print(df.head(),'\n\n')
sns.countplot(df['fruit_name'],label="Count")
df=df.select_dtypes(exclude=['object'])

X_train, X_test, y_train, y_test = train_test_split(df.iloc[:,1:], df['fruit_label'],random_state=60, test_size=.2)


training_acc=[]
test_acc=[]
k_range=range(1,11)

scaler=StandardScaler()
X_train_scale=scaler.fit_transform(X_train)
X_test_scale=scaler.transform(X_test)



for n_neighbors in k_range:
    clf=KNeighborsClassifier(n_neighbors=n_neighbors)
    clf.fit(X_train_scale, y_train)
    training_acc.append(clf.score(X_train_scale, y_train))
    test_acc.append(clf.score(X_test_scale, y_test))

plt.plot(k_range,training_acc,label='training accuracy')
plt.plot(k_range,test_acc, label='test accuracy')
plt.ylabel("Accuracy")
plt.xlabel("neighbors")
plt.legend()
plt.show()


clf=KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train_scale, y_train)
print('Accuracy of K-N classifier on training set: ',format(clf.score(X_train_scale, y_train)*100),'%')
print('Accuracy of K-N classifier on test set: ',format(clf.score(X_test_scale, y_test)*100),'%')

#Example
arr=np.array([[130,7.6,0.5,0.86],[216,7.3,10.2,0.71]])
print('Predict given values by K-N Classifier:\n',arr)
arr = scaler.transform(arr)
print(clf.predict(arr),'\n\n')
print('-----------------------------------------------------------------------------------------------\n\n')



# KNC got test accuracy of 100% and train accuracy of 97.87%



X_train, X_test, y_train, y_test = train_test_split(df.iloc[:,1:], df['fruit_label'],random_state=60, test_size=0.20)
X_train_scale1=scaler.fit_transform(X_train)
X_test_scale1=scaler.transform(X_test)


training_acc=[]
test_acc=[]
k_range= np.arange(0.1,1.5,0.1)
for i in k_range:
    logreg=LogisticRegression(C=i)
    logreg.fit(X_train_scale1, y_train)
    training_acc.append(logreg.score(X_train_scale1, y_train))
    test_acc.append(logreg.score(X_test_scale1, y_test))

plt.scatter(k_range,training_acc,c='k',label='training accuracy')
plt.scatter(k_range,test_acc,c='r',label='test accuracy')
plt.ylabel('Accuracy',c='k')
plt.xlabel('settings',c='r')
plt.legend()
plt.show()


training_acc=[]
test_acc=[]
k_range=np.arange(1,100,20)

for i in k_range:
    logreg=LogisticRegression(C=i)
    logreg.fit(X_train_scale1, y_train)
    training_acc.append(logreg.score(X_train_scale1, y_train))
    test_acc.append(logreg.score(X_test_scale1, y_test))

plt.scatter(k_range,training_acc,c='k',label="training accuracy")
plt.scatter(k_range,test_acc,c='r',label="test accuracy")
plt.ylabel('Accuracy',c='k')
plt.xlabel('settings',c='r')
plt.legend()
plt.show()


logreg=LogisticRegression(C=0.7)
logreg.fit(X_train_scale1,y_train)
print('Accuracy of Logistic Regression Classifier on Training Set: %',format(logreg.score(X_train_scale1, y_train)*100),'%')
print('Accuracy of Logistic Regression Classifier on Test Set: %',format(logreg.score(X_test_scale1, y_test)*100),'%')



#logistic regression got test accuracy of 75% and train accuracy of 78.72% 


#Example
arr=np.array([[130,7.6,0.5,0.86],[216,7.3,10.2,0.71]])
print('Predict given values by Logistic Regression Classifier:\n' ,arr)
arr=scaler.transform(arr)
print(logreg.predict(arr))


#################################################################################
#Based on accuracy, K Neighbors Classification is better than Logistic Regression.
#Prediction is good too.


# In[ ]:





# In[ ]:




