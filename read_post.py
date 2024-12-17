import praw

# Set up Reddit API client
reddit = praw.Reddit(
    client_id="bqwbGIUUup1mn3_Pt_cyiw",
    client_secret="	GvMAb-9Y3arpcM34VsoybWJ6VqrTgQ",
    user_agent="script:crud:v1.0 (by /u/BigRaspberry2255)",
    username="BigRaspberry2255",
    password="reddit17"
)

# Function to fetch posts by the authenticated user
def get_user_posts(subreddit_name=None, post_limit=5):
    try:
        user = reddit.user.me()
        
        # Fetch posts by the user
        user_posts = user.submissions.new(limit=post_limit)
        
        # Store post data in a list of dictionaries
        posts_data = []
        
        count = 0
        for post in user_posts:
            # Filter by subreddit if a specific one is provided
            if subreddit_name and post.subreddit.display_name.lower() != subreddit_name.lower():
                continue
            
            count += 1
            posts_data.append({
                'title': post.title,
                'score': post.score,
                'url': post.url,
                'content': post.selftext[:200]  # Truncate to 200 characters
            })
        
        print(f"Fetched {count} posts.")
        
        return posts_data  # Return posts data
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

