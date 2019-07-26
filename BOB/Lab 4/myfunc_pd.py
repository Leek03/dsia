#!/usr/bin/env python
# coding: utf-8

# In[3]:


'''
Cenral Limit Theoram

Simulated sampling (sample mean)

Now, we'd like to get an idea of what happens when we take multiple random samples of size 5.

Take 10 sample (size=5) from the entire population. Calculate means for each sample. Now make a histogram of all the sample means.

Describe the shape of the histogram.
What is the center of the distribution of sample means?

'''
def calculate_sample_mean(df, column_name, N=10, sample_size=5):
    '''
    df: DataFrame
    column_name: String, column_name
    N: Number of samples
    sample_size: Size of sample for each sample
    '''
    sample_mean_list = []

    for i in range(N):
        df_sample = df.sample(n=sample_size)
        sample_mean = df_sample[column_name].mean()
        sample_mean_list.append(sample_mean)
    
    return sample_mean_list


# In[ ]:





# In[4]:


'''
Visulize the sample mean and the dataset mean in the same histplot

'''
def visual_sample_mean(population_mean, sample_mean_list):
    '''
    population_mean: mean of entire population
    sample_mean_list: list of sample mean
    '''
    
    sample_mean = np.mean(sample_mean_list)
    
    ax = sns.distplot(sample_mean_list);
    
    # plot a vertical line for population mean and sample mean
    ax.axvline(population_mean, color='black', linestyle='solid', lw=1)
    ax.axvline(sample_mean, color='red', linestyle='dashed', lw=1)
    
    plt.xlabel('Mean of Samples')
    plt.ylabel('Frequency')

    plt.show()


# In[ ]:


'''
Cleaning the author name

calling funtion as df['Author'] = df['Author'].apply(clean_author_names)

'''

def clean_author_names(author):
    
    author = str(author)
    
    if author == 'nan':
        return 'NaN'
    
    author = author.split(',')

    if len(author) == 1:
        name = filter(lambda x: x.isalpha(), author[0])
        return reduce(lambda x, y: x + y, name)
    
    last_name, first_name = author[0], author[1]

    first_name = first_name[:first_name.find('-')] if '-' in first_name else first_name
    
    if first_name.endswith(('.', '.|')):
        parts = first_name.split('.')
        
        if len(parts) > 1:
            first_occurence = first_name.find('.')
            final_occurence = first_name.find('.', first_occurence + 1)
            first_name = first_name[:final_occurence]
        else:
            first_name = first_name[:first_name.find('.')]
    
    last_name = last_name.capitalize()
    
    return f'{first_name} {last_name}'


# In[ ]:


'''
Clean title for some title with by, By, []..

calling funtion as 

df['Title'] = df['Title'].apply(clean_title)


'''

def clean_title(title):
    
    if title == 'nan':
        return 'NaN'
    
    if title[0] == '[':
        title = title[1: title.find(']')]
        
    if 'by' in title:
        title = title[:title.find('by')]
    elif 'By' in title:
        title = title[:title.find('By')]
        
    if '[' in title:
        title = title[:title.find('[')]

    title = title[:-2]
        
    title = list(map(str.capitalize, title.split()))
    return ' '.join(title)
    


# In[ ]:


'''
Datas cleaning 

df ---------- DataFrame
col ---------- the name of column , as 'dates'

calling funtion as 

df['Date of Publication'] = df.apply(clean_dates, axis = 1)

'''



def clean_dates(df, col):
    
    unwanted_characters = ['[', ',', '-']
    
    dop= str(df.loc[col])
    
    if dop == 'nan' or dop[0] == '[':
        return np.NaN
    
    for character in unwanted_characters:
        if character in dop:
            character_index = dop.find(character)
            dop = dop[:character_index]
    
    return dop


# In[2]:


'''
CUT Function ---  To make new category 

col ----------- column as df['AB']
bins -----------  How many you want to cut as 2
labels ----------  giving the list of labels as ['z','z']

Calling as 

bikes['atemp_level'] = cut_add_new_category (bikes['atemp'], bins = 4, labels = ["cool", "mild", "warm", "hot"])
    

** Set-up a new column to store



'''

def cut_add_new_category( col, N, labels ):
    
    atemp_level = pd.cut(col, bins = N, labels = labels)
    
    return atemp_level
          


# In[1]:


'''
Define the outlier for each column 

3 sigma boundary

Calling as outlier_datapoints = detect_outlier(df['AAA'])
'''

def outlier_detect(data):
   
    import numpy as np
    import pandas as pd
    outliers=[]
    
    
    threshold=3
    mean_1 = np.mean(data)
    std_1 =np.std(data)
    
    
    for y in data:
        z_score= (y - mean_1)/std_1 
        if np.abs(z_score) > threshold:
            outliers.append(y)
    return outliers
            


# In[ ]:


'''
Normalize data process:

Default value input is df['AAA']

'''

def NormData(s,low='min',center='mid',hi='max',insideout=False,shrinkfactor=0.):    
    if low=='min':
        low=min(s)
    elif low=='abs':
        low=max(abs(min(s)),abs(max(s)))*-1.#sign(min(s))
    if hi=='max':
        hi=max(s)
    elif hi=='abs':
        hi=max(abs(min(s)),abs(max(s)))*1.#sign(max(s))

    if center=='mid':
        center=(max(s)+min(s))/2
    elif center=='avg':
        center=np.mean(s)
    elif center=='median':
        center=np.median(s)

    s2=[x-center for x in s]
    hi=hi-center
    low=low-center
    center=0.

    r=[]

    for x in s2:
        if x<low:
            r.append(0.)
        elif x>hi:
            r.append(1.)
        else:
            if x>=center:
                r.append((x-center)/(hi-center)*0.5+0.5)
            else:
                r.append((x-low)/(center-low)*0.5+0.)

    if insideout==True:
        ir=[(1.-abs(z-0.5)*2.) for z in r]
        r=ir

    rr =[x-(x-0.5)*shrinkfactor for x in r]    
    return rr


# In[2]:


'''
To find the best features for linear regression:

Need to set-up the dataframe name df....

X-train, X_test, y_train, y_test




'''


def linear_best_feature(df,X_test,X_train,y_train):
    
    import pandas as pd
    import matplotlib.pyplot as plt
    from sklearn import linear_model


    ## Flag intermediate output

    show_steps = False   # for testing/debugging
    # show_steps = False  # without showing steps
    
    
    ## Use Forward Feature Selection to pick a good model

    # start with no predictors
    included = []
    # keep track of model and parameters
    best = {'feature': '', 'r2': 0, 'a_r2': 0}
    # create a model object to hold the modelling parameters
    model = linear_model.LinearRegression()
    # get the number of cases in the test data
    n = X_test.shape[0]
    
    r2_list = []
    adjusted_r2_list = []
    
    
    
    while True:
        
        
        changed = False
    
        if show_steps:
            print('') 

        # list the features to be evaluated
        excluded = list(set(df.columns) - set(included))
        
        if show_steps:
            print('(Step) Excluded = %s' % ', '.join(excluded))  

        # for each remaining feature to be evaluated
        for new_column in excluded:
            
            if show_steps:
                
                print('(Step) Trying %s...' % new_column)
                print('(Step) - Features = %s' % ', '.join(included + [new_column]))

            # fit the model with the Training data
            fit = model.fit(X_train[included + [new_column]], y_train)
            # calculate the score (R^2 for Regression)
            r2 = fit.score(X_train[included + [new_column]], y_train)
        
            # number of predictors in this model
            k = len(included) + 1
            # calculate the adjusted R^2
            adjusted_r2 = 1 - ( ( (1 - r2) * (n - 1) ) / (n - k - 1) )
        
            if show_steps:
                print('(Step) - Adjusted R^2: This = %.3f; Best = %.3f' % 
                      (adjusted_r2, best['a_r2']))

            # if model improves
            if adjusted_r2 > best['a_r2']:
                # record new parameters
                best = {'feature': new_column, 'r2': r2, 'a_r2': adjusted_r2}
                # flag that found a better model
                changed = True
                if show_steps:
                    print('(Step) - New Best!   : Feature = %s; R^2 = %.3f; Adjusted R^2 = %.3f' % 
                          (best['feature'], best['r2'], best['a_r2']))
        # END for
    
        r2_list.append(best['r2'])
        adjusted_r2_list.append(best['a_r2'])

    # if found a better model after testing all remaining features
        if changed:
        # update control details
            included.append(best['feature'])
            excluded = list(set(excluded) - set(best['feature']))
            print('Added feature %-4s with R^2 = %.3f and adjusted R^2 = %.3f' % 
                  (best['feature'], best['r2'], best['a_r2']))
        else:
            # terminate if no better model
            print('*'*50)
            break

    print('')
    print('Resulting features:')
    print(', '.join(included))

    ## Chart both R^2 and Adjusted R^2

    _range = range(1, len(r2_list)+1)

    # define chart size
    plt.figure(figsize = (10, 5))
# plot each metric 
    plt.plot(_range, r2_list, label = '$R^2$')
    plt.plot(_range, adjusted_r2_list, label = '$Adjusted \: R^2$')
# add some better visualisation
    plt.xlabel('Number of Features')
    plt.legend()
# output the chart
    plt.show()
    
    
    
    
    
    


# In[ ]:




