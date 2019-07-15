#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 11:46:10 2019

@author: weinazhu1
"""

#! usr/bin/env python3
import praw
import pandas as pd
import datetime as dt




subreddit = reddit.subreddit('Nootropics')

top_subreddit = subreddit.top()


top_subreddit = subreddit.top(limit=500)


for submission in subreddit.top(limit=1):
    print(submission.title, submission.id)
    
    
topics_dict = { "title":[], "score":[],  "id":[], "url":[],  "comms_num": [], "created": [],"body":[]}


import sqlite3

connection = sqlite3.connect("mydatabase1.db")
c = connection.cursor()
query = "CREATE TABLE taula(title string, score int, id string,  url string ,comms_num int, body string,created string )"
c.execute(query)

for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)
    
    query = "INSERT INTO taula (title, score, id,  url ,comms_num, body,created) VALUES (?,?,?,?,?,?,?)"
    data =(submission.title, submission.score, submission.id,submission.url,submission.num_comments,submission.selftext,submission.created)
    
    c.execute(query,data)

    connection.commit()

topics_data = pd.DataFrame(topics_dict)





def get_date(created):
    return dt.datetime.fromtimestamp(created)

_timestamp = topics_data["created"].apply(get_date)


topics_data = topics_data.assign(timestamp = _timestamp)



topics_data.to_csv('reddit_top_500.csv', index=False) 





