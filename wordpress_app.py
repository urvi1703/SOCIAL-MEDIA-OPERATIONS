import streamlit as st
import requests
from requests.auth import HTTPBasicAuth

# WordPress API credentials
API_URL = "https://your-wordpress-site.com/wp-json/wp/v2/posts"
USERNAME = "your-wordpress-username"
PASSWORD = "your-application-password"

# Functions for CRUD operations
def create_post(title, content):
    payload = {"title": title, "content": content, "status": "publish"}
    response = requests.post(API_URL, auth=HTTPBasicAuth(USERNAME, PASSWORD), json=payload)
    return response.status_code, response.json()

def read_posts():
    response = requests.get(API_URL, auth=HTTPBasicAuth(USERNAME, PASSWORD))
    return response.status_code, response.json()

def update_post(post_id, title, content):
    payload = {"title": title, "content": content}
    response = requests.post(f"{API_URL}/{post_id}", auth=HTTPBasicAuth(USERNAME, PASSWORD), json=payload)
    return response.status_code, response.json()

def delete_post(post_id):
    response = requests.delete(f"{API_URL}/{post_id}?force=true", auth=HTTPBasicAuth(USERNAME, PASSWORD))
    return response.status_code, response.json()

# Streamlit UI
st.title("WordPress Blog Manager")

# Sidebar for navigation
menu = st.sidebar.selectbox("Menu", ["Create", "Read", "Update", "Delete"])

# Create Post
if menu == "Create":
    st.subheader("Create a New Blog Post")
    title = st.text_input("Post Title")
    content = st.text_area("Post Content")
    if st.button("Create"):
        if title and content:
            status_code, response = create_post(title, content)
            if status_code == 201:
                st.success(f"Post '{response['title']['rendered']}' created successfully!")
            else:
                st.error(f"Failed to create post: {response}")
        else:
            st.error("Title and content cannot be empty!")

# Read Posts
elif menu == "Read":
    st.subheader("View Blog Posts")
    status_code, posts = read_posts()
    if status_code == 200:
        for post in posts:
            st.markdown(f"### {post['title']['rendered']}")
            st.write(post['content']['rendered'])
            st.markdown("---")
    else:
        st.error("Failed to fetch posts!")

# Update Post
elif menu == "Update":
    st.subheader("Update an Existing Blog Post")
    status_code, posts = read_posts()
    if status_code == 200 and posts:
        post_id = st.selectbox("Select Post to Update", [post['id'] for post in posts])
        selected_post = next(post for post in posts if post['id'] == post_id)
        new_title = st.text_input("New Title", selected_post['title']['rendered'])
        new_content = st.text_area("New Content", selected_post['content']['rendered'])
        if st.button("Update"):
            if new_title and new_content:
                status_code, response = update_post(post_id, new_title, new_content)
                if status_code == 200:
                    st.success(f"Post '{response['title']['rendered']}' updated successfully!")
                else:
                    st.error(f"Failed to update post: {response}")
            else:
                st.error("Title and content cannot be empty!")
    else:
        st.info("No posts available to update.")

# Delete Post
elif menu == "Delete":
    st.subheader("Delete a Blog Post")
    status_code, posts = read_posts()
    if status_code == 200 and posts:
        post_id = st.selectbox("Select Post to Delete", [post['id'] for post in posts])
        if st.button("Delete"):
            status_code, response = delete_post(post_id)
            if status_code == 200:
                st.success("Post deleted successfully!")
            else:
                st.error(f"Failed to delete post: {response}")
    else:
        st.info("No posts available to delete.")
