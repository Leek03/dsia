#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 11:15:28 2019

@author: weinazhu1
"""
"https://apps.reddit.com/\n"

"pip install praw

#! usr/bin/env python3
import praw
import pandas as pd
import datetime as dt

#! Create path to RedditAPI Note: keep 'password' safe can direct to a reading-file i.e. Json
reddit = praw.Reddit(client_id='RmQSwN_rMMz1oA', \
                     client_secret='myJoHIigoKfxXsFbyg2hcBBUnUQ', \
                     user_agent='ISTANBUL INVESTA', \
                     username='weinazhu', \
                     password='redditapikey1')

subreddit = reddit.subreddit('Nootropics')

top_subreddit = subreddit.top()

top_subreddit = subreddit.top(limit=500)

for submission in subreddit.top(limit=1):
    print(submission.title, submission.id)
    
topics_dict = { "title":[], \
                "score":[], \
                "id":[], "url":[],  
                "comms_num": [], \
                "created": [], \
                "body":[]}

for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)
    
topics_data = pd.DataFrame(topics_dict)
topics_data

def get_date(created):
    return dt.datetime.fromtimestamp(created)

_timestamp = topics_data["created"].apply(get_date)

topics_data = topics_data.assign(timestamp = _timestamp)
topics_data

topics_data.to_csv('RedditAPP-Nootropics-Case.csv', index=False) 
