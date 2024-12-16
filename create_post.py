import praw

# Set up Reddit API client
reddit = praw.Reddit(
    client_id="bqwbGIUUup1mn3_Pt_cyiw",
    client_secret="GvMAb-9Y3arpcM34VsoybWJ6VqrTgQ",
    user_agent="script:Content manager:v1.0 (by /u/BigRaspberry2255)",
    username="BigRaspberry2255",
    password="Reddit1703"
)

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

