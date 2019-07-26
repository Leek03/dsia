# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 12:00:18 2019

@author: DataLoungeUser
"""
import numpy as np
import pandas as pd
import seaborn as sns
#import plotly
#%matplotlib inline
#import plotly.plotly as py
import matplotlib.pyplot as plt
from matplotlib import style

from sklearn.model_selection import train_test_split

style.use('fivethirtyeight')

df = pd.read_csv("housingdata.csv",header = 0)

df.head()

housing_colnames = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
df.columns = housing_colnames
df.info()
df.head()
colnames = df.columns
print(colnames)

df_A,df_test = train_test_split(df, test_size=0.20, random_state=42)
df_train,df_val = train_test_split(df_A, test_size=0.20, random_state=42)


def plotFeatures(col_list,title):
   plt.figure(figsize=(10, 14))
   i = 0
   print(len(col_list))
   for col in col_list:
       i+=1
       plt.subplot(10,2,i)
       plt.plot(df[col],df["MEDV"],marker='.',linestyle='none')
       plt.title(title % (col))
       plt.tight_layout()


#colnames = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
plotFeatures(colnames,"Relationship bw %s and MEDV")

#plt.matshow(df.corr()) 
#diagram to compare with each other Hieu Understand
fig = plt.subplots(figsize = (10,10))
sns.set(font_scale=1.5)
sns.heatmap(df.corr(),square = True,cbar=True,annot=True,annot_kws={'size': 10})
plt.show()

def predictPrice(x,theta):
    return np.dot(x,theta)


def calculateCost(x,theta,Y):
    prediction = predictPrice(x,theta)
    return ((prediction - Y)**2).mean()/2

def abline(x,theta,Y):
    """Plot a line from slope and intercept"""
    
    y_vals = predictPrice(x,theta)
    plt.xlim(0, 20)
    plt.ylim(-10, 60)
    plt.xlabel('No. of Rooms in the house')
    plt.ylabel('Price of house')
    plt.gca().set_aspect(0.1, adjustable='datalim')
    plt.plot(x,Y,'.',x, y_vals, '-')
    plt.show()
    

def gradientDescentLinearRegression(alpha=0.001,iter=20000): # alpha learning rate and iter is the time it will run. 
    '''initialized the values'''
    theta = np.zeros(2)
    prev_val = 1
    counter =0
    theta0 = []
    theta1 = []
    costs_train = []
    costs_val = []
    
    '''provide the training information Hieu Understand'''
    predictor = df_train["MEDV"]
    x_train = np.column_stack((np.ones(len(predictor)),predictor))
    Y_train = df_train["MEDV"]
    
    '''provide the validation information Hieu Understand'''
    predictor_val = df_val["MEDV"]
    x_val = np.column_stack((np.ones(len(predictor_val)),predictor_val))
    Y_val = df_val["MEDV"]
           
    '''Do for number of iter'''
    for i in range(iter):
        '''do the prediction'''
        pred = predictPrice(x_train,theta)
        '''' correct the gradient '''
        t0 = theta[0] - alpha *(pred - Y_train).mean()
        t1 = theta[1] - alpha *((pred - Y_train)* x_train[:,1]).mean()
        theta = np.array([t0,t1])
        
        ''' training loss '''
        J_train = calculateCost(x_train,theta,Y_train)
        theta0.append(t0)
        theta1.append(t1)
        costs_train.append(J_train)
        '''validation loss'''
        J_val = calculateCost(x_val,theta,Y_val)
        costs_val.append(J_val)
        if i%1000==0:
            print(f"Iteration: {i+1},Cost = {J_train},theta = {theta}")
            
            print(f"Iteration: {i+1},Cost_val = {J_val},theta = {theta}")
            
            abline(x_train,theta,Y_train)
        if J_val>prev_val:
            counter +=1   #counter = counter + 1
            prev_val = J_val
        else:
            counter = 0
            prev_val = J_val
            
        '''check the termination condition''' 
        if counter>10:
            print ("terminated")
            print(f'theta0 = {len(theta0)}\ntheta1 = {len(theta1)}\nCosts = {len(costs_train)}')
            print ( J_val,prev_val,counter,i)
            return costs_val,costs_train,theta,i+1
        
#            abline(x_train,theta,Y_train)
    print(f'theta0 = {len(theta0)}\ntheta1 = {len(theta1)}\nCosts = {len(costs_train)}')
    return costs_val,costs_train,theta,iter
        
#    print(f'theta0 = {len(theta0)}\ntheta1 = {len(theta1)}\nCosts = {len(costs_val)}')
    
costs_val,costs_train,theta,iteration  = gradientDescentLinearRegression()
'''prepare the test data'''

predictor_test = df_test["RM"]
x_test = np.column_stack((np.ones(len(predictor_test)),predictor_test))
Y_test = df_test["MEDV"]  

'''Calculate the loss for test data'''
J_test = calculateCost(x_test,theta,Y_test)
print(f"Iteration: {iter},Cost_test = {J_test},theta = {theta}")
'''plot the test data'''
y_test_vals = predictPrice(x_test,theta)
plt.xlim(0, 20) ## plot x limit from 0 to 20 
plt.ylim(-10, 60) ## plot y limit from -10 to 60 
plt.xlabel('No. of Rooms in the house')
plt.ylabel('Price of house')
plt.gca().set_aspect(0.1, adjustable='datalim')
plt.plot(x_test,Y_test,'.',x_test, y_test_vals, '-')
plt.show()

''' create range of iteration'''
x=list(range(0, iteration))
'''plot the loss information'''

plt.xlabel('No. of iteration')
plt.ylabel('Loss')
plt.plot(x,costs_train,'.',x, costs_val, '-')
plt.show()
