# Reddit r/coronavirus Scraper
This project includes a scraper for data from the r/coronavirus subreddit and some elementary analysis into trends from the data.
The project consists of two parts: the scraper, in `RedditScraper.py`, and the data analysis, in `RedditAnalyzer.py`, both of which are to be run from the command line.

## RedditScraper.py
To use this program, you must have a `praw.ini` file with the parmeters needed to log into and use the Reddit API.
These parameters should be stored under the `[scraperbot]` header.
Go to https://www.reddit.com/prefs/apps, log in and create an app with script permissions to get Reddit access tokens, and go to https://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html for information on `praw.ini` files.
A template `praw.ini` file is included in this repository under `praw_template.ini`.

This program takes a random sample of 1500 posts from the subreddit r/coronavirus and saves their data to `data.json`.
Any duplicate posts are ignored, which resulted in only around 350 posts being saved to the file.
The json file is a dump of a Python dict, with the Reddit post ID as the key and a dict of information (`"title": <string>, "timestamp": "%Y-%m-%d %H:%M:%S", "author": <string>, "score": <int>`) as the value.

Unfortunately, due to Reddit API limitations, it isn't possible (to my knowledge) to be able to scrape all of the posts on r/coronavirus.
Therefore, I expected random sampling to give a good indication of the population of posts on the sub.

## RedditAnalyzer.py
This program takes in the data from `data.json`, analyzes the data, and saves the results into json files.
These files are named `data_<subject>.json`, and exist for `words` in the title of posts, `authors`, and `dates` of posts.
Within `data_words.json` and `data_authors.json` exists a list of `(word, count)` or `(author, count)` tuples, sorted in decreasing order based on count.
`data_dates.json` contains a dict of dates and the count of posts on that date.

## Analysis of the data
Overall, there were 354 posts analyzed.
340 of these were posted on May 10, 2020, and 14 were posted on May 9, 2020.
Of the 354 posts sampled, user u/156497 posted the most with 59, followed by u/helenolai with 31, u/maize-n-blue97 with 27, u/vergil_never_cry with 13, and u/KushN16 with 12.
The most common words used in the subreddit titles, excluding "coronavirus" and variations thereof and prepositions<sup>1</sup>, were "new" with 57 occurrences, "cases" with 45, "more" with 25, "deaths" with 23, and "reports" with 21.

## Issues with this project
As mentioned above, due to the limitations of the Reddit API, I was only able to analyze around 350 posts through random sampling.
Of these, 96 percent were posted on May 10, and the rest were posted on May 9.
This sample is missing a very large portion of the data set, and because of this, I feel it is not a very accurate depiction of the entire subreddit as a whole.
In addition, the randomness of Reddit's random post feature appears to heavily bias towards recent posts, so much so that none of the posts returned came from before May 9, 2020.
Because of this, it was difficult to receive a good sample of posts from the subreddit, which led to a limited amount of data.

## Potential Areas for Improvement
Most of the improvements for this project would come in the form of improving the data.
However, due to the limitations of Reddit itself, it is not likely that this will be doable.

Some potential improvements for the program itself would be to allow access to different subreddits, allow access to different post selection methods (e.g., hot, new, top all time, etc.), and allow access to a different number of posts (up to 1000, the Reddit API limit).
However, it would likely have been more of a hassle to use these, so I chose to maintain the ease of use the program currently has.



<sup>1</sup> All words excluded from this list include ["to", 134], ["coronavirus", 122], ["the", 100], ["in", 98], ["of", 96], ["covid-19", 94], ["and", 47], ["for", 46], ["a", 44], ["after", 29], ["on", 28], ["as", 28], ["is", 28], ["from", 24] 