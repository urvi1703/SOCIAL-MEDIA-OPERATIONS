import praw

# Set up Reddit API client

# Create a post with user input
def create_reddit_post(subreddit_name, title, content):
    try:
        # Make the post
        subreddit = reddit.subreddit(subreddit_name)
        subreddit.submit(title, selftext=content)
        print("Post created successfully!")
        return "Post created successfully!"
    except Exception as e:
        print(f"An error occurred: {e}")
        return f"An error occurred: {e}"

