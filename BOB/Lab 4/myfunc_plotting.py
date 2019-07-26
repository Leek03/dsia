#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import numpy as np
import seaborn as sns


# In[ ]:





# In[6]:


def plot_two_hist(col_1, label_1,col_2, label_2):
    '''
    col_1, col_2 are the series of pd.DataFrame
    
    label_1, label_2 are the name shown.
    '''
    
    ax = sns.distplot(col_1, label=label_1, kde=False);
    sns.distplot(col_2, ax=ax, label=label_2, kde=False);
    plt.legend(loc = 'upper right')
    plt.xlabel('')
    plt.ylabel('')
    plt.show();


# In[7]:


'''
Plotting the heat_map for the dataset
df: the name of dataframe
title: 'This is the title'
'''

def heat_map_plot(df,title):
    f, ax = plt.subplots(figsize=(10, 6))
    corr = df.corr()
    hm = sns.heatmap(round(corr,2), annot=True, ax=ax, cmap="coolwarm",fmt='.2f',linewidths=.05)
    f.subplots_adjust(top=0.93)
    t= f.suptitle(title, fontsize=14)


# In[8]:


'''
Pair_wise plot
df ----- the dataframe
c_N ------ the name of column with ''
title ------ title with ''

'''

def pair_plot_multi(df, c_1,c_2, c_3, c_4, title ):
    cols = [c_1, c_2, c_3, c_4]
    pp = sns.pairplot(df[cols], size=1.8, aspect=1.8,
                      plot_kws=dict(edgecolor="k", linewidth=0.5),
                      diag_kind="kde", diag_kws=dict(shade=True))
    fig = pp.fig 
    fig.subplots_adjust(top=0.93, wspace=0.3)
    t = fig.suptitle(title, fontsize=14)


# In[9]:


'''
To plot the two Continuing numerical value by using sns

col_1, col_2 ------ the column in dataframe df['']

x_label,y_label,title ------- always come with ''

'''
def scatter_plot(col_1, col_2,x_label,y_label,title):
    plt.scatter(col_1, col_2,
                alpha=0.4, edgecolors='w')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title,y=1.05)


# In[10]:


'''
Joint-plot ------ scatter plot with hist
col_1, col_2 -----  the name of column, just use 'ABC'
data --------- the name of dataframe ,,, df


'''

def joint_plot(col_1, col_2, data):
    sns.jointplot(x=col_1, y=col_2, data=data,kind='reg', space=0, size=5, ratio=4)


# In[11]:


'''
Count_plot ------ plot count of each category 
col ------- the name of column with '', for counting
hue -------- the name of column with '', as different category 
data . ------- the dataframe, as df
'''

def count_plot(col,hue,data):
    sns.countplot(x=col, hue=hue, data=data, 
                   palette={"red": "#FF9999", "white": "#FFE888"});


# In[1]:


'''
Box-plot for multiple columns together

category ------ as the x-axis seperate the data into different categories, come with 'AB'
col ----------- as the y-axis the value always come with column name as 'AB'
data -----------  as df

x_label, ylabel
'''

def box_plot_multi(category,col,data,x_label,y_label):
    f, (ax) = plt.subplots(1, 1, figsize=(12, 4))
    f.suptitle(title, fontsize=14)
    
    sns.boxplot(x=category, y=col, data=data,  ax=ax)
    ax.set_xlabel(x_label,size = 12,alpha=0.8)
    ax.set_ylabel(y_label,size = 12,alpha=0.8)


# In[13]:


'''
Atttibute in 3D 
c1..c4 ------- the name of column, come with ''
hue ---------- the name of column as a kind of category , come with ''
data . ---------  df 
title ------------  'ABB'

'''
def attribute_three_dimension(c1, c2, c3, c4, hue,data,title):
    
    cols = [c1, c2, c3, c4, hue]
    pp = sns.pairplot(data[cols], hue=hue, size=1.8, aspect=1.8, 
                      palette={"red": "#FF9999", "white": "#FFE888"},
                      plot_kws=dict(edgecolor="black", linewidth=0.5))
    fig = pp.fig 
    fig.subplots_adjust(top=0.93, wspace=0.3)
    t = fig.suptitle(title, fontsize=14)


# In[14]:


'''
3D Three_Continuous_Numeric_attributes 

c_x,c_y,c_z ------------ The column name in x,y,z. come with df['A']

x_label,y_label,z_label --------- the info add into x,y,z, come with 'AAA'

'''

def Three_Continuous_Numeric_attributes(c_x,c_y,c_z,x_label,y_label,z_label):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    xs = c_x
    ys = c_y
    zs = c_z
    ax.scatter(xs, ys, zs, s=50, alpha=0.6, edgecolors='w')
    
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_zlabel(z_label)


# In[17]:


'''
Scatter in 3D 

c_1, c_2, c_3 ---------- The column in dataframe, come with df['A']
scale -------------   the scale that depends on the value of c_3, to make it larger
x_label, y_label, title ------------- come with 'AA'

'''

def scatter_three_dimension (c_1, c_2, c_3, scale, x_label, y_label, title):
    plt.scatter(c_1, c_2, s= c_3*scale, 
                alpha=0.4, edgecolors='w')

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title,y=1.05)


# In[ ]:




