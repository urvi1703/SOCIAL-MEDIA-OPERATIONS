import streamlit as st
import requests

# Replace with your actual access token and Instagram User ID
ACCESS_TOKEN = 'EAAYUYyDfveEBO12KOhmt8V75b30i8KfZBMy5N9mFnuvRYHMNFCcTd8QUr6ixtQqdNswOElXo8QhHXkuL5PbiWN2EBZAPkCgLfM02ckV8j7c70ZCyNUXAL40XXgZAYiQdek1KvGP5xbsHYNLIZAHOiwQ0yvs8HrGgouPT3ORBU7NxnhQUuZBYI6uUdU6sHy41fH'
IG_USER_ID = '493274720537567'

BASE_URL = f"https://graph.facebook.com/v17.0/{IG_USER_ID}"

# Streamlit UI for creating a post
def create_post():
    st.write("Choose the type of post you want to create:")
    post_type = st.selectbox("Post Type", ["Text Post", "Post with Image", "Post with Video"])

    if post_type == "Text Post":
        message = st.text_input("Enter the message you want to post:")
        if st.button("Create Text Post"):
            if message:
                url = f"{BASE_URL}/feed"
                params = {'message': message, 'access_token': ACCESS_TOKEN}
                try:
                    response = requests.post(url, params=params, timeout=30)
                    response.raise_for_status()
                    st.success("Text Post Created Successfully!")
                except requests.exceptions.RequestException as e:
                    st.error(f"Error: {e}")
    
    elif post_type == "Post with Image":
        image_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png", "gif"])
        caption = st.text_input("Enter a caption for the image:")
        if st.button("Create Image Post"):
            if image_file:
                url = f"{BASE_URL}/photos"
                params = {'caption': caption, 'access_token': ACCESS_TOKEN}
                try:
                    # Upload image to Instagram
                    files = {'source': image_file}
                    response = requests.post(url, params=params, files=files, timeout=30)
                    response.raise_for_status()
                    st.success("Image Post Created Successfully!")
                except requests.exceptions.RequestException as e:
                    st.error(f"Error: {e}")
    
    elif post_type == "Post with Video":
        video_file = st.file_uploader("Choose a video", type=["mp4", "mov", "avi", "mkv"])
        description = st.text_input("Enter a description for the video:")
        if st.button("Create Video Post"):
            if video_file:
                url = f"{BASE_URL}/videos"
                params = {'description': description, 'access_token': ACCESS_TOKEN}
                try:
                    # Upload video to Instagram
                    files = {'source': video_file}
                    response = requests.post(url, params=params, files=files, timeout=30)
                    response.raise_for_status()
                    st.success("Video Post Created Successfully!")
                except requests.exceptions.RequestException as e:
                    st.error(f"Error: {e}")
    
    else:
        st.error("Invalid post type selected.")

# Streamlit UI for reading posts
def read_posts():
    url = f"{BASE_URL}/media"
    params = {'access_token': ACCESS_TOKEN}
    try:
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        st.write("Read Posts:")
        posts = response.json().get('data', [])
        for post in posts:
            st.write(f"Post ID: {post['id']}")
            st.write(f"Caption: {post.get('caption', 'No caption available')}")
            st.write(f"Media URL: {post['media_url']}")
            st.write(f"Timestamp: {post['timestamp']}")
            st.write("-" * 20)
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")

# Streamlit UI for updating a post
def update_post():
    post_id = st.text_input("Enter the Post ID you want to update:")
    new_message = st.text_input("Enter the new message:")
    if st.button("Update Post"):
        if post_id and new_message:
            url = f"https://graph.facebook.com/{post_id}"
            params = {
                'message': new_message,
                'access_token': ACCESS_TOKEN
            }
            try:
                response = requests.post(url, params=params, timeout=30)
                response.raise_for_status()
                st.success("Post Updated Successfully!")
            except requests.exceptions.RequestException as e:
                st.error(f"Error: {e}")
        else:
            st.error("Post ID and new message are required.")

# Streamlit UI for deleting a post
def delete_post():
    post_id = st.text_input("Enter the Post ID you want to delete:")
    if st.button("Delete Post"):
        if post_id:
            url = f"https://graph.facebook.com/{post_id}"
            params = {'access_token': ACCESS_TOKEN}
            try:
                response = requests.delete(url, params=params, timeout=30)
                response.raise_for_status()
                st.success("Post Deleted Successfully!")
            except requests.exceptions.RequestException as e:
                st.error(f"Error: {e}")
        else:
            st.error("Post ID is required.")

# Streamlit UI for following a user
def follow_user():
    user_id = st.text_input("Enter the User ID to follow:")
    if st.button("Follow User"):
        if user_id:
            url = f"https://graph.facebook.com/v17.0/{IG_USER_ID}/following"
            params = {'user_id': user_id, 'access_token': ACCESS_TOKEN}
            try:
                response = requests.post(url, params=params, timeout=30)
                response.raise_for_status()
                st.success("User Followed Successfully!")
            except requests.exceptions.RequestException as e:
                st.error(f"Error: {e}")

# Streamlit UI for unfollowing a user
def unfollow_user():
    user_id = st.text_input("Enter the User ID to unfollow:")
    if st.button("Unfollow User"):
        if user_id:
            url = f"https://graph.facebook.com/v17.0/{IG_USER_ID}/following/{user_id}"
            params = {'access_token': ACCESS_TOKEN}
            try:
                response = requests.delete(url, params=params, timeout=30)
                response.raise_for_status()
                st.success("User Unfollowed Successfully!")
            except requests.exceptions.RequestException as e:
                st.error(f"Error: {e}")

# Streamlit UI for viewing profile status
def view_profile_status():
    url = f"https://graph.facebook.com/v17.0/{IG_USER_ID}"
    params = {
        'fields': 'id,username,name,profile_picture_url,biography,website',
        'access_token': ACCESS_TOKEN
    }
    try:
        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        profile_info = response.json()
        st.write("Profile Status:")
        st.write(f"Username: {profile_info['username']}")
        st.write(f"Name: {profile_info['name']}")
        st.write(f"Biography: {profile_info.get('biography', 'No bio')}")
        st.write(f"Website: {profile_info.get('website', 'No website')}")
        st.image(profile_info['profile_picture_url'], caption="Profile Picture")
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")

# Streamlit UI for changing profile picture
def change_profile_picture():
    image_file = st.file_uploader("Choose a new profile picture", type=["jpg", "jpeg", "png"])
    if st.button("Change Profile Picture"):
        if image_file:
            url = f"https://graph.facebook.com/v17.0/{IG_USER_ID}"
            params = {'access_token': ACCESS_TOKEN}
            files = {'source': image_file}
            try:
                response = requests.post(url, params=params, files=files, timeout=30)
                response.raise_for_status()
                st.success("Profile Picture Changed Successfully!")
            except requests.exceptions.RequestException as e:
                st.error(f"Error: {e}")

# Main Streamlit UI
def main():
    st.title("Instagram Post Management App")
    
    menu = ["Create a Post", "Read Posts", "Update a Post", "Delete a Post", "Follow a User", 
            "Unfollow a User", "View Profile Status", "Change Profile Picture", "Exit"]
    choice = st.sidebar.selectbox("Choose an operation", menu)
    
    if choice == "Create a Post":
        create_post()
    elif choice == "Read Posts":
        read_posts()
    elif choice == "Update a Post":
        update_post()
    elif choice == "Delete a Post":
        delete_post()
    elif choice == "Follow a User":
        follow_user()
    elif choice == "Unfollow a User":
        unfollow_user()
    elif choice == "View Profile Status":
        view_profile_status()
    elif choice == "Change Profile Picture":
        change_profile_picture()
    elif choice == "Exit":
        st.write("Exiting the program.")

# Run the app
if __name__ == "__main__":
    main()
