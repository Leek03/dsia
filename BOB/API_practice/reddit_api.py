#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 10:32:41 2019

@author: bob
"""


import pandas as pd
import datetime as dt
import praw
import time
import sqlite3

reddit = praw.Reddit(client_id='ze9HIBPNs8AtSg', \
                     client_secret='P1LuJX-1lIyPhZbp2iY3QpwF-8c', \
                     user_agent='BOBBBB', \
                     username='BOB0807', \
                     password='wojshiwO0807')
subreddit = reddit.subreddit('sydney')



top_subreddit = subreddit.top(limit=500)
# for item in top_subreddit:
#     print(item.title)

sqlite_db = 'test_db_reddit.sqlite'
conn = sqlite3.connect(sqlite_db)
c = conn.cursor()





topics_dict = {"title":[],"score":[],"id":[],"url":[],"comms_num":[],"created":[],"body":[]}

query = 'CREATE TABLE Reddit_new(title string, score int, id string,  url string ,comms_num int, body string,created string)'

c.execute(query)
conn.commit()



for submission in top_subreddit:

    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)
    query_1 = 'INSERT INTO Reddit_new (title, score, id, url, comms_num, created, body) VALUES(?,?,?,?,?,?,?)'
    data = (submission.title,submission.score,submission.id,submission.url,submission.num_comments,submission.created,submission.selftext)
    c.execute(query_1,data)
# for i,v in topics_dict.items():
#     print(i,v)





topics_data = pd.DataFrame(topics_dict)
topics_data.head()

def get_date(created):
   return dt.datetime.fromtimestamp(created)

_timestamp = topics_data["created"].apply(get_date)


topics_data = topics_data.assign(timestamp = _timestamp)



# topics_data.to_csv('FILENAME.csv', index=False)

























