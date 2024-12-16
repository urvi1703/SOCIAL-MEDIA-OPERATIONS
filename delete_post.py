import praw

# Set up Reddit API client
reddit = praw.Reddit(
    client_id="K1rhO5hjcgWr86L0kW5pjQ",
    client_secret="KVWREayY7U1_OFzkQlKz00AFW0rXQQ",
    user_agent="script:crud:v1.0 (by u/Holiday-Box3743)",
    username="Holiday-Box3743",
    password="soumya2854"
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


