# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 12:39:00 2019

@author: ET
"""

import pandas as pd


datafile = "train.csv"
data = pd.read_csv(datafile)


data1 = data.drop(['Name', 'Ticket', 'Cabin'], axis=1)
#print (data1)
#
#
#
#cat_columns = df.select_dtypes(['category']).columns
#
#cat_columns
#Index([u'col2', u'col3'], dtype='object')
#
#df[cat_columns] = df[cat_columns].apply(lambda x: x.cat.codes)
#
#
#X = data1.iloc[:,:].values
#
#
#
#from sklearn.preprocessing import LabelEncoder
#labelencoder_X=LabelEncoder()
#X[:,0] = labelencoder_X.fit_transform(X[:,0])
#
#
#print (X)

data1.fillna(0)
data_features = data1.drop(columns='Survived')
data_out = pd.DataFrame(columns=['Survived'])
data_out['Survived'] = data1['Survived']

'''convert to numeric value'''
#cols = df.columns.tolist()
data_features['Sex'] = data_features['Sex'].astype('category')

data_features['Embarked'] = data_features['Embarked'].astype('category')

cat_columns = data_features.select_dtypes(['category']).columns

#Index([u'Sex', u'Embarked'], dtype='object')

data_features[cat_columns] = data_features[cat_columns].apply(lambda x: x.cat.codes)

'''

'''

'''Normalize the data'''

from sklearn import preprocessing

x = data_features.values #returns a numpy array
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
data_features2 = pd.DataFrame(x_scaled)


data_averege = pd.DataFrame(columns=['mean'])
data_averege['mean'] = data_features2.mean(axis=1)


data_final =pd.DataFrame(columns=['mean','Survived'])
data_final = pd.concat([data_averege, data_out], ignore_index=True, sort =False)

data_final.fillna(0)
##Create a boxplot
#data.boxplot('weight', by='group', figsize=(12, 8))
ctrl = data_final['mean'][data_final.Survived == 1]
 
grps = pd.unique(data_final.Survived.values)
d_data = {grp:data_final['mean'][data_final.Survived == grp] for grp in grps}
# 
#k = len(pd.unique(data_final.Survived))  # number of conditions
#N = len(data_final.values)  # conditions times participants
#n = data_final.groupby('Survived').size()[0] #Participants in each condition
#
#








from scipy import stats
 
F, p = stats.f_oneway(d_data[0], d_data[1])

print (F,p)









