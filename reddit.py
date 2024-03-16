import praw
import os
from dotenv import load_dotenv
load_dotenv()
reddit= praw.Reddit(
    client_id= os.getenv('REDDIT_CLIENT_ID'),
    client_secret= os.getenv('REDDIT_CLIENT_SECRET'),
    user_agent=os.getenv('REDDIT_USER_AGENT'),
)

reddit.read_only=True

submissions = reddit.subreddit('UpliftingNews').hot(limit=5)

for submission in submissions:
    print(submission.title)


