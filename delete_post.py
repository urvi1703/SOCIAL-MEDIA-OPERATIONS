import praw

# Set up Reddit API client
reddit = praw.Reddit(
    client_id="bqwbGIUUup1mn3_Pt_cyiw",
    client_secret="	GvMAb-9Y3arpcM34VsoybWJ6VqrTgQ",
    user_agent="script:crud:v1.0 (by /u/BigRaspberry2255)",
    username="BigRaspberry2255",
    password="reddit17"
)

# Function to delete a Reddit post
def delete_reddit_post(post_id):
    try:
        # Fetch the post by ID
        post = reddit.submission(id=post_id)
        
        # Check if the post exists
        if not post:
            return "Invalid Post ID or the post does not exist."
        
        # Check if the authenticated user is the author
        if post.author.name != reddit.user.me().name:
            return "You can only delete posts that you have created."
        
        # Delete the post
        post.delete()
        return "Post deleted successfully!"
    
    except Exception as e:
        return f"An error occurred: {e}"


