#!/usr/bin/env python
# coding: utf-8

# In[119]:


#Name:                   Nikita Singh
#Roll Number:            20075060
#Branch and section:     CSE Btech BA1
#Email:                  nikita.singh.cse20@itbhu.ac.in

                                     #PROBLEM 2
    
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split    
from sklearn import preprocessing
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

df=pd.read_csv('Problem2.csv')
print(df.head(),'\n\n')

X_train,X_test,y_train,y_test= train_test_split(df.iloc[:,:9],df['Outcome'],random_state=0,test_size=0.30)
clf=KNeighborsClassifier()
clf.fit(X_train,y_train)

y_predtest=clf.predict(X_test)
y_predtrain=clf.predict(X_train)
val1=metrics.accuracy_score(y_test,y_predtest)
val2=metrics.accuracy_score(y_train,y_predtrain)
print('KN classifier training data accuracy is: ',val2*100)
print('KN classifier test data accuracy is: ',val1*100,'%\n\n')


#############################################################


import seaborn as sns
sns.countplot(df['Outcome'],label='Count')

plt.figure(figsize=(10,10))
plt.subplot(3,3,1)
sns.barplot(x='Outcome',y='Glucose',data=df,hue='Outcome')
plt.subplot(3,3,2)
sns.barplot(x='Outcome',y='Insulin',data=df,hue='Outcome')
plt.subplot(3,3,3)
sns.barplot(x='Outcome',y='SkinThickness',data=df,hue='Outcome')
plt.subplot(3,3,4)
sns.barplot(x='Outcome',y='BMI',data=df,hue='Outcome')
plt.subplot(3,3,5)
sns.barplot(x='Outcome',y='DiabetesPedigreeFunction',data=df,hue='Outcome')
plt.subplot(3,3,6)
sns.barplot(x='Outcome',y='Age',data=df,hue='Outcome')
sns.catplot(x='Pregnancies',y='BloodPressure',data=df,hue='Outcome')

training_acc=[]
test_acc=[]
neighbors_settings=list(range(1,10))

scaler=StandardScaler()
X_train_scale=scaler.fit_transform(X_train)
X_test_scale=scaler.transform(X_test)

for n_neighbors in neighbors_settings:
    knc = KNeighborsClassifier(n_neighbors=n_neighbors)
    knc.fit(X_train, y_train)
    training_acc.append(knc.score(X_train, y_train))
    test_acc.append(knc.score(X_test, y_test))

plt.plot(neighbors_settings,training_acc,label='training accuracy')
plt.plot(neighbors_settings,test_acc,label='test accuracy')
plt.ylabel('Accuracy')
plt.xlabel('n_neighbors')
plt.legend()
plt.show()


# 
