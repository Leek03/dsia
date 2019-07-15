#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on Fri Jul 12 18:40:02 2019

@author: hieu
'''

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

ckey="dvGM4S03FWCbU4Am5LuhKlWa2"
csecret="oHkbyaA5WbqLAcmnG01fQUXOFn5Se9HmSPXNisQtqT6k5QeeIe"
atoken="977026214081708032-xw6VUC5nwwgS1MDlaCXJ1YmqI04I7h6"
asecret="V4kvwVJiQuzimM9slZXL37VMtvn5vPk1xqYr9uXjAUlCz"

#This is a basic listener that just prints tweets to Stdoutlistener
class Stdoutlistener(StreamListener):

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

if __name__ == '__main__':
    #this handles Twitter authetication and the connection to Twitter Streaming API
    l = Stdoutlistener()
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    stream = Stream(auth,l)
    
    #this line filter Twitter Streams to capture data by the keywords:'python', 'ruby', 'javascript'
    stream.filter(track=['python', 'ruby', 'javascript'])
