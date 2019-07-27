# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 10:19:16 2019

@author: tilee
"""

import numpy as np

import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt



df = pd.read_csv('../_datasets/iris.csv')

np.values = df.iloc[:,0:4].values
np.mean(np_values[:,0])

# Create bee swarm plot with Seaborn's default settings

sns.swarmplot(x='species', y='petal length (cm)', data=df)



# Label the axes

plt.xlabel('species')

plt.ylabel('petal length (cm)')



# Show the plot

plt.show()
versicolor_petal_length = np.array([4.7,  4.5,  4.9,  4.,  4.6,  4.5,  4.7,  3.3,  4.6,  3.9,  3.5,

                                    4.2,  4.,  4.7,  3.6,  4.4,  4.5,  4.1,  4.5,  3.9,  4.8,  4.,

                                    4.9,  4.7,  4.3,  4.4,  4.8,  5.,  4.5,  3.5,  3.8,  3.7,  3.9,

                                    5.1,  4.5,  4.5,  4.7,  4.4,  4.1,  4.,  4.4,  4.6,  4.,  3.3,

                                    4.2,  4.2,  4.2,  4.3,  3.,  4.1])



# Compute the mean: mean_length_vers

mean_length_vers = np.mean(versicolor_petal_length)



# Print the result with some nice formatting

print('I. versicolor:', mean_length_vers, 'cm')




