import json
import praw
from datetime import datetime as dt

# I am using a praw.ini file to contain all of the parameters needed
# to log in to Reddit. These are stored under the "scraperbot" header
# in the ini file. These tokens are not included for security reasons.
# Go to https://www.reddit.com/prefs/apps, log in and create an app with
# script permissions to get Reddit access tokens.

# The json file of data I collected is saved at data.json

posts = {}

# Create read-only Reddit instance
reddit = praw.Reddit("scraperbot")
reddit.read_only = True
subreddit = reddit.subreddit("coronavirus")

# Select 1500 random posts
for i in range(1500):
    post = subreddit.random()
    try:
        post_data = {"title": post.title, 
                     "timestamp": dt.fromtimestamp(post.created_utc).strftime("%Y-%m-%d %H:%M:%S"),
                     "author": post.author.name,
                     "score": post.score}
        # Add non duplicate posts to the dataset
        if post.id not in posts:
            posts[post.id] = post_data
    except:  # post is invalid
        pass

# Save to file
with open("data.json", "w") as fp:
    json.dump(posts, fp)
