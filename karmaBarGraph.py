import praw
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


reddit = praw.Reddit("A reddit karma visualizer by Sandesh")

user_name = raw_input("Please enter a reddit username? ")

redditor = reddit.get_redditor(user_name)
content = redditor.get_submitted(limit=None)

karma = {}

for thing in content:
    subreddit = thing.subreddit.display_name
    karma[subreddit] = (karma.get(subreddit, 0) + thing.score)
  

objects = list(karma.keys())
y_pos = np.arange(len(objects))
performance =  list(karma.values())
 
plt.barh(y_pos, performance, align='center', alpha=0.5)
plt.yticks(y_pos, objects)
plt.xlabel('Karma')
title = "Subreddit Bar Graph for reddit user: " + user_name
plt.title(title)
 
plt.show()



