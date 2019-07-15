#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 11:42:58 2019

@author: weinazhu1
"""

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming imort StreamListener

class listener(StreamListener):
    
    def on_data(self, data):
        print(data)
        # read the data by json
        all_data = json.loads(data)
        tweet = all_data['text']
        username = all_data['user'], ['screen_name'])
        query = "INSERT INTO taula (time, username, tweet) VALUES(?,?,?)"
        data =(time.time(), username, tweet)
        
        c.execute(query,data)
        
        connection.commit()
        
        return(True)
        
        def on_error(self, status):
            print("1111")
            print(status)
       