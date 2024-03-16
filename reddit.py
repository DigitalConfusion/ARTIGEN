import praw

reddit= praw.Reddit(
    client_id="CLIENT_ID",
    client_secret="CLIENT_SECRET",
    user_agent="ARTIGEN",
)

reddit.read_only=True

submissions = reddit.subreddit('UpliftingNews').hot(limit=5)
for submission in submissions:
    print(submission.title)


