#! python3
import praw
import pandas as pd
import datetime as dt

# I am using a praw.ini file to contain all of the parameters needed
# to log in to Reddit. These are stored under the "scraperbot" header.

# Create read-only Reddit instance
reddit = praw.Reddit("scraperbot")
reddit.read_only = True

subreddit = reddit.subreddit("coronavirus")
top_subreddit = subreddit.top()
print (top_subreddit)