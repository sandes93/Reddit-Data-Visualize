import praw


reddit = praw.Reddit("A reddit bot by Sandesh")

user_name = raw_input("Please enter a reddit username? ")

redditor = reddit.get_redditor(user_name)
content = redditor.get_submitted(limit=None)

subKarma = {}

for thing in content:
    subreddit = thing.subreddit.display_name
    subKarma[subreddit] = (subKarma.get(subreddit, 0) + thing.score)



for subreddit in subKarma:
    print '"{name}": {subKarma},'.format(name=subreddit, subKarma=subKarma[subreddit])