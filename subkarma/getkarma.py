import praw


reddit = praw.Reddit("A reddit bot by Sandesh")

user_name = raw_input("Please enter a reddit username? ")

redditor = reddit.get_redditor(user_name)
content = redditor.get_submitted(limit=None)

karma = {}

count=0


for thing in content:
    subreddit = thing.subreddit.display_name
    karma[subreddit] = (karma.get(subreddit, 0) + thing.score)
    count+=1
    if count==8:
    	break

ascendingKarma = sorted(karma, key=lambda x : karma[x])

obj = ""

for subreddit in ascendingKarma:
    obj+= '"{name}": {karma},'.format(name=subreddit, karma=karma[subreddit])

print obj