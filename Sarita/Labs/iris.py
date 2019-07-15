# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 10:26:15 2019

@author: praty
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('iris.csv')
#convert to numpy

np_values=df.iloc[:,0:4].values
print(np.mean(np_values[:,0]))
# Create bee swarm plot with Seaborn's default settings
sns.swarmplot(x='variety', y='petal.length', data=df)

# Label the axes
plt.xlabel('variety')
plt.ylabel('petal.length')

# Show the plot
plt.show()