import os
import requests

# Access token and Instagram User ID (Replace with your values)
ACCESS_TOKEN = "EAAYUYyDfveEBO5gFpViUUpVQSMD0YXjktZCOWmAJWSlgBNZANRiN1CbLhQYpWZBqbihBh7yLy4k8NXAIDPMdWcSrDpry48bU4VnEvwRELtzlgyhfdqiMHcaM09d40CPGuMEluOoB1m34lD1tHVKhtkVfZA1KP1jOhZAFrHFZBuw3oAU5OUqqmtpIyx6qnHRJZCG"
IG_USER_ID = "17841471294584311"

def create_post(media_url, caption, media_type="image"):
    """
    Create an Instagram post using a media URL and caption.
    """
    if media_type not in ["image", "video"]:
        return "Invalid media type. Use 'image' or 'video'."

    # Step 1: Create Media Container
    media_endpoint = f"https://graph.facebook.com/v17.0/{IG_USER_ID}/media"
    params = {
        "caption": caption,
        "access_token": ACCESS_TOKEN,
    }
    if media_type == "image":
        params["image_url"] = media_url
    elif media_type == "video":
        params["video_url"] = media_url

    response = requests.post(media_endpoint, data=params)
    if response.status_code != 200:
        return f"Error creating media container: {response.json().get('error', {}).get('message')}"

    creation_id = response.json().get("id")

    # Step 2: Publish Media
    publish_endpoint = f"https://graph.facebook.com/v17.0/{IG_USER_ID}/media_publish"
    publish_params = {
        "creation_id": creation_id,
        "access_token": ACCESS_TOKEN,
    }
    publish_response = requests.post(publish_endpoint, data=publish_params)
    if publish_response.status_code == 200:
        return "Post created successfully!"
    else:
        return f"Error publishing post: {publish_response.json().get('error', {}).get('message')}"

def read_posts():
    """
    Fetch all Instagram posts for the user.
    """
    url = f"https://graph.facebook.com/v17.0/{IG_USER_ID}/media"
    params = {
        "fields": "id,caption,media_type,media_url,timestamp",
        "access_token": ACCESS_TOKEN,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get("data", [])
    else:
        return f"Error fetching posts: {response.json().get('error', {}).get('message')}"

def delete_post(post_id):
    """
    Delete a specific post using its ID.
    """
    url = f"https://graph.facebook.com/v17.0/{post_id}"
    params = {"access_token": ACCESS_TOKEN}
    response = requests.delete(url, params=params)
    if response.status_code == 200:
        return "Post deleted successfully!"
    else:
        return f"Error deleting post: {response.json().get('error', {}).get('message')}"

def like_post(post_id):
    """
    Like a specific post using its ID.
    """
    url = f"https://graph.facebook.com/v17.0/{post_id}/likes"
    params = {"access_token": ACCESS_TOKEN}
    response = requests.post(url, data=params)
    if response.status_code == 200:
        return "Post liked successfully!"
    else:
        return f"Error liking post: {response.json().get('error', {}).get('message')}"

def comment_on_post(post_id, comment):
    """
    Add a comment to a specific post using its ID.
    """
    url = f"https://graph.facebook.com/v17.0/{post_id}/comments"
    params = {
        "message": comment,
        "access_token": ACCESS_TOKEN,
    }
    response = requests.post(url, data=params)
    if response.status_code == 200:
        return "Comment added successfully!"
    else:
        return f"Error adding comment: {response.json().get('error', {}).get('message')}"

def follow_user(user_id):
    """
    Follow a user using their ID.
    """
    url = f"https://graph.facebook.com/v17.0/{IG_USER_ID}/following"
    params = {
        "user_id": user_id,
        "access_token": ACCESS_TOKEN,
    }
    response = requests.post(url, data=params)
    if response.status_code == 200:
        return "User followed successfully!"
    else:
        return f"Error following user: {response.json().get('error', {}).get('message')}"

def unfollow_user(user_id):
    """
    Unfollow a user using their ID.
    """
    url = f"https://graph.facebook.com/v17.0/{IG_USER_ID}/following/{user_id}"
    params = {"access_token": ACCESS_TOKEN}
    response = requests.delete(url, params=params)
    if response.status_code == 200:
        return "User unfollowed successfully!"
    else:
        return f"Error unfollowing user: {response.json().get('error', {}).get('message')}"

def view_profile_status():
    """
    View Instagram profile information.
    """
    url = f"https://graph.facebook.com/v17.0/{IG_USER_ID}"
    params = {
        "fields": "id,username,name,profile_picture_url,biography,website",
        "access_token": ACCESS_TOKEN,
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error fetching profile info: {response.json().get('error', {}).get('message')}"

def change_profile_picture(image_url):
    """
    Change Instagram profile picture.
    """
    url = f"https://graph.facebook.com/v17.0/{IG_USER_ID}"
    payload = {
        "profile_picture_url": image_url,
        "access_token": ACCESS_TOKEN,
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        return "Profile picture changed successfully!"
    else:
        return f"Error changing profile picture: {response.json().get('error', {}).get('message')}"

def main():
    """
    Command-line interface for Instagram CRUD operations.
    """
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
            media_url = input("Enter media URL: ")
            media_type = input("Enter media type ('image' or 'video'): ").strip().lower()
            caption = input("Enter caption: ")
            print(create_post(media_url, caption, media_type))

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
                print(f"Name: {profile_info.get('name', 'N/A')}")
                print(f"Bio: {profile_info.get('biography', 'N/A')}")
                print(f"Website: {profile_info.get('website', 'N/A')}")
                print(f"Profile Picture: {profile_info.get('profile_picture_url', 'N/A')}")
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

if __name__ == "__main__":
    main()
