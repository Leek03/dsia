#!/usr/bin/env python
# coding: utf-8

# # Streaming Tweets from Twitter to Database
# 
# 

# Streaming tweets from the Twitter API v1.1
# 
# First let's cover streaming tweets from Twitter. You're going to need a Twitter dev account. Sometimes Twitter uses dev.twitter.com to advertise various things they expect devs to be interested in. The problem is they sometimes make it hard to get to where you want to be. Just in case they've done this and the video's method isn't available, here's the link: Twitter Apps
# https://apps.twitter.com/
# 

# Next, make a new application, filling in your name, description, website, agree to their terms, do the captcha, and create the application.

# Once submitted successfully, you should be presented with a page where you can see your consumer key and consumer secret. Now you need an access token, so scroll down and click on "create my access token."
# 
# After a few moments, refresh, and you should be able to see the access key and access token. Once you have that, you're going to need to get Tweepy, which is a Python module for streaming Twitter tweets.
# 
# It is probably easiest to download and install Tweepy via pip if you're using a current version of Python.
# 
# pip install tweepy

# You can also install using the setup.py method that I used in the video.
# 
# Once you have Tweepy, let's show a very basic example of its use:

# First, We should import the package for streaming tweets from Twitter.

# In[6]:


from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sqlite3
import date

# Then, We need to insert access info.
# #consumer key, consumer secret, access token, access secret.

# In[7]:


my_consumer_key = '4xPV0tmdlrb5ZQsOVqXpgmCNV'
my_consumer_secret = 'rABwgPQZJAxRRTLhbIvXg8IcrWJGDRg0MC5LLnrLy8Nph98Q0z'
my_access_token = '977026214081708032-IUrnQhQenKoNJTvQIlaIyvrK30vgHLF'      
access_token_secret = 'OWOAjae42eJAHHeVkGaCUF43ebEAmSIu4nA53RNYipb6U'


# We need to define a class to listen to the tweets in Twitter

# In[ ]:




# In[8]:


class listener(StreamListener):

    def on_data(self, data):
        print(data)
        # read the data by json
        all_data = json.loads(data)
        tweet = all_data["text"]
        #username = all_data["user"]["screen_name"]
        print(tweet)

        
        return(True)

    def on_error(self, status):
        
        print (status)


# Now, we can call the authenticator API for validating the access to Twitter.

# In[9]:


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)


# Finally, We can Listen to tweets :)
# 
# We just want to listen the tweets about the F1 racing.
# 

# In[11]:


twitterStream = Stream(auth, listener())
twitterStream.filter(track=["F1"])


# for the second task, we aim to creat a log from the tweets, to do the further process in the future. We use the sqlite3 for SQL processing.
# 

# In[12]:


#import sqlite3


# In[ ]:


#Creat  connection



# In[20]:


connection = sqlite3.connect("hieutrantwit.db")
c = connection.cursor()


# Create a table to save tweets

# In[21]:


query = "CREATE TABLE taula(time string, username string, tweet string)"
c.execute(query)


# We creat another listener for saving the tweet info

# In[ ]:





# In[22]:


class listener1(StreamListener):

    def on_data(self, data):
#        print(data)

        all_data = json.loads(data)
        tweet = all_data["text"]
        username = all_data["user"]["screen_name"]
        # use the insert into command to add reccords.
        query = "INSERT INTO taula (time, username, tweet) VALUES (?,?,?)"
        data =(date.time(), username, tweet)

        c.execute(query,data)

        connection.commit()

        return(True)

    def on_error(self, status):
        print("1111")
        print (status)


# Now, we can call the authenticator API for validating the access to Twitter.

# In[23]:


twitterStream1 = Stream(auth, listener1())
twitterStream1.filter(track=["iran"])


# if you would like to know about the content of the database.

# In[ ]:


connection = sqlite3.connect("hieutrantwit.db")
c = connection.cursor()

query = "select * from taula"
zz=c.execute(query)


for row in zz:
   print ("time = ", row[0])
   print ("username = ", row[1])
   print ("tweet = ", row[2])
print ("Operation done successfully");
connection.close()


