import os
import requests

# Access token and Instagram User ID (You need to replace these with your values)
ACCESS_TOKEN = "EAAYUYyDfveEBO12KOhmt8V75b30i8KfZBMy5N9mFnuvRYHMNFCcTd8QUr6ixtQqdNswOElXo8QhHXkuL5PbiWN2EBZAPkCgLfM02ckV8j7c70ZCyNUXAL40XXgZAYiQdek1KvGP5xbsHYNLIZAHOiwQ0yvs8HrGgouPT3ORBU7NxnhQUuZBYI6uUdU6sHy41fH"
IG_USER_ID = "493274720537567"

# Create Post (Upload image/video with caption)
def create_post(file_path_or_url, caption, media_type="image"):
    """
    Create an Instagram post with either an uploaded file or a URL.
    """
    if os.path.isfile(file_path_or_url):  # Check if it's a file path
        upload_url = f"https://graph.facebook.com/v17.0/{IG_USER_ID}/media"
        with open(file_path_or_url, "rb") as media_file:
            files = {"file": media_file}
            payload = {
                "caption": caption,
                "media_type": media_type,
                "access_token": ACCESS_TOKEN,
            }
            response = requests.post(upload_url, files=files, data=payload)
    else:  # Assume it's a URL
        upload_url = f"https://graph.facebook.com/v17.0/{IG_USER_ID}/media"
        payload = {
            "image_url" if media_type == "image" else "video_url": file_path_or_url,
            "caption": caption,
            "access_token": ACCESS_TOKEN,
        }
        response = requests.post(upload_url, data=payload)

    if response.status_code == 200:
        media_id = response.json()["id"]
        publish_url = f"https://graph.facebook.com/v17.0/{IG_USER_ID}/media_publish"
        publish_payload = {"creation_id": media_id, "access_token": ACCESS_TOKEN}
        publish_response = requests.post(publish_url, data=publish_payload)
        if publish_response.status_code == 200:
            return "Post created successfully!"
        else:
            return f"Error publishing post: {publish_response.text}"
    else:
        return f"Error uploading media: {response.text}"

# Read Posts (Fetch all posts)
def read_posts():
    url = f"https://graph.facebook.com/v17.0/{IG_USER_ID}/media"
    params = {
        "fields": "id,caption,media_type,media_url,timestamp",
        "access_token": ACCESS_TOKEN,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("data", [])
    else:
        return f"Error fetching posts: {response.text}"

# Delete Post (Delete a post using post ID)
def delete_post(post_id):
    url = f"https://graph.facebook.com/v17.0/{post_id}"
    params = {"access_token": ACCESS_TOKEN}
    response = requests.delete(url, params=params)
    if response.status_code == 200:
        return "Post deleted successfully!"
    else:
        return f"Error deleting post: {response.text}"

# Like a Post (Like a post using post ID)
def like_post(post_id):
    url = f"https://graph.facebook.com/v17.0/{post_id}/likes"
    params = {"access_token": ACCESS_TOKEN}
    response = requests.post(url, params=params)
    if response.status_code == 200:
        return "Post liked successfully!"
    else:
        return f"Error liking post: {response.text}"

# Comment on a Post (Comment on a post using post ID)
def comment_on_post(post_id, message):
    url = f"https://graph.facebook.com/v17.0/{post_id}/comments"
    params = {"message": message, "access_token": ACCESS_TOKEN}
    response = requests.post(url, params=params)
    if response.status_code == 200:
        return "Comment added successfully!"
    else:
        return f"Error adding comment: {response.text}"

# Follow a User (Follow a user using their ID)
def follow_user(user_id):
    url = f"https://graph.facebook.com/v17.0/{IG_USER_ID}/following"
    params = {"user_id": user_id, "access_token": ACCESS_TOKEN}
    response = requests.post(url, params=params)
    if response.status_code == 200:
        return "User followed successfully!"
    else:
        return f"Error following user: {response.text}"

# Unfollow a User (Unfollow a user using their ID)
def unfollow_user(user_id):
    url = f"https://graph.facebook.com/v17.0/{IG_USER_ID}/following/{user_id}"
    params = {"access_token": ACCESS_TOKEN}
    response = requests.delete(url, params=params)
    if response.status_code == 200:
        return "User unfollowed successfully!"
    else:
        return f"Error unfollowing user: {response.text}"

# View Profile Status (View your Instagram profile information)
def view_profile_status():
    url = f"https://graph.facebook.com/v17.0/{IG_USER_ID}"
    params = {
        "fields": "id,username,name,profile_picture_url,biography,website",
        "access_token": ACCESS_TOKEN,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error fetching profile info: {response.text}"

# Change Profile Picture (Change DP)
def change_profile_picture(image_url):
    url = f"https://graph.facebook.com/v17.0/{IG_USER_ID}"
    payload = {
        "profile_picture_url": image_url,
        "access_token": ACCESS_TOKEN,
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        return "Profile picture changed successfully!"
    else:
        return f"Error changing profile picture: {response.text}"

# Main function for CRUD operations
def main():
    print("Instagram CRUD Operations")

    while True:
        print("\nSelect an operation:")
        print("1. Create Post")
        print("2. Read Posts")
        print("3. Delete Post")
        print("4. Like Post")
        print("5. Comment on Post")
        print("6. Follow User")
        print("7. Unfollow User")
        print("8. View Profile Status")
        print("9. Change Profile Picture")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            file_path_or_url = input("Enter file path or URL: ")
            media_type = input("Enter media type ('image' or 'video'): ").strip().lower()
            caption = input("Enter caption: ")
            print(create_post(file_path_or_url, caption, media_type))

        elif choice == "2":
            posts = read_posts()
            if isinstance(posts, list):
                for post in posts:
                    print(f"ID: {post['id']}")
                    print(f"Caption: {post.get('caption', 'No caption')}")
                    print(f"URL: {post['media_url']}")
                    print(f"Timestamp: {post['timestamp']}")
                    print("-" * 20)
            else:
                print(posts)

        elif choice == "3":
            post_id = input("Enter Post ID to delete: ")
            print(delete_post(post_id))

        elif choice == "4":
            post_id = input("Enter Post ID to like: ")
            print(like_post(post_id))

        elif choice == "5":
            post_id = input("Enter Post ID to comment on: ")
            comment = input("Enter your comment: ")
            print(comment_on_post(post_id, comment))

        elif choice == "6":
            user_id = input("Enter User ID to follow: ")
            print(follow_user(user_id))

        elif choice == "7":
            user_id = input("Enter User ID to unfollow: ")
            print(unfollow_user(user_id))

        elif choice == "8":
            profile_info = view_profile_status()
            if isinstance(profile_info, dict):
                print(f"Username: {profile_info['username']}")
                print(f"Name: {profile_info['name']}")
                print(f"Biography: {profile_info.get('biography', 'No bio')}")
                print(f"Website: {profile_info.get('website', 'No website')}")
                print(f"Profile Picture URL: {profile_info['profile_picture_url']}")
            else:
                print(profile_info)

        elif choice == "9":
            image_url = input("Enter new profile picture URL: ")
            print(change_profile_picture(image_url))

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
