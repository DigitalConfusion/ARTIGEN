import praw
import os
from dotenv import load_dotenv
load_dotenv()

def getTitles():
    reddit= praw.Reddit(
        client_id= os.getenv('REDDIT_CLIENT_ID'),
        client_secret= os.getenv('REDDIT_CLIENT_SECRET'),
        user_agent=os.getenv('REDDIT_USER_AGENT'),
    )

    reddit.read_only=True

    submissions = reddit.subreddit('Art').top(time_filter='day', limit=15)

    promptamSutam = []
    for submission in submissions:
        #print(submission.title.split(',')[0])
        promptamSutam.append(submission.title.split(',')[0])
    print(promptamSutam)
    return(promptamSutam)
getTitles()



