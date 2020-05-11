import json
import operator
from datetime import datetime as dt

with open("data.json", "r") as fp:
    data = json.load(fp)

words = {}
authors = {}
dates = {}
for key in data:
    # Words in Posts
    title = data[key]["title"]
    title_words = title.split()
    for word in title_words:
        if word.lower() not in words:
            words[word.lower()] = 0
        words[word.lower()] += 1

    # Authors of Posts
    author = data[key]["author"]
    if author not in authors:
        authors[author] = 0
    authors[author] += 1

    # Date of Posts
    date_and_time = dt.strptime(data[key]["timestamp"], "%Y-%m-%d %H:%M:%S")
    date = date_and_time.date()
    date_string = dt.strftime(date, "%Y-%m-%d")
    if date_string not in dates:
        dates[date_string] = 0
    dates[date_string] += 1

sorted_words = sorted(words.items(), key=operator.itemgetter(1), reverse=True)
sorted_authors = sorted(authors.items(), key=operator.itemgetter(1), reverse=True)

with open("data_words.json", "w") as fp:
    json.dump(sorted_words, fp)
with open("data_authors.json", "w") as fp:
    json.dump(sorted_authors, fp)
with open("data_dates.json", "w") as fp:
    json.dump(dates, fp)
