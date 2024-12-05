import streamlit as st
import requests
from requests.auth import HTTPBasicAuth

# WordPress API credentials
WP_API_URL = "https://your-wordpress-site.com/wp-json/wp/v2/posts"
WP_USERNAME = "your-username"
WP_PASSWORD = "your-application-password"

# CRUD Operations
def create_post(title, content):
    payload = {"title": title, "content": content, "status": "publish"}
    response = requests.post(WP_API_URL, auth=HTTPBasicAuth(WP_USERNAME, WP_PASSWORD), json=payload)
    return response.status_code, response.json()

def read_posts():
    response = requests.get(WP_API_URL, auth=HTTPBasicAuth(WP_USERNAME, WP_PASSWORD))
    return response.status_code, response.json()

def update_post(post_id, title, content):
    payload = {"title": title, "content": content}
    response = requests.post(f"{WP_API_URL}/{post_id}", auth=HTTPBasicAuth(WP_USERNAME, WP_PASSWORD), json=payload)
    return response.status_code, response.json()

def delete_post(post_id):
    response = requests.delete(f"{WP_API_URL}/{post_id}?force=true", auth=HTTPBasicAuth(WP_USERNAME, WP_PASSWORD))
    return response.status_code, response.json()

# Main function for WordPress integration
def main():
    st.subheader("WordPress CRUD Operations")
    
    menu = st.sidebar.radio("WordPress Menu", ["Create", "Read", "Update", "Delete"])
    
    if menu == "Create":
        title = st.text_input("Post Title")
        content = st.text_area("Post Content")
        if st.button("Create Post"):
            if title and content:
                status_code, response = create_post(title, content)
                if status_code == 201:
                    st.success(f"Post '{response['title']['rendered']}' created successfully!")
                else:
                    st.error(f"Error: {response}")
            else:
                st.warning("Title and content are required.")
    
    elif menu == "Read":
        status_code, posts = read_posts()
        if status_code == 200:
            for post in posts:
                st.markdown(f"### {post['title']['rendered']}")
                st.write(post['content']['rendered'])
                st.markdown("---")
        else:
            st.error("Failed to retrieve posts.")

    elif menu == "Update":
        status_code, posts = read_posts()
        if status_code == 200:
            post_id = st.selectbox("Select Post to Update", [post['id'] for post in posts])
            selected_post = next(post for post in posts if post['id'] == post_id)
            new_title = st.text_input("New Title", selected_post['title']['rendered'])
            new_content = st.text_area("New Content", selected_post['content']['rendered'])
            if st.button("Update Post"):
                status_code, response = update_post(post_id, new_title, new_content)
                if status_code == 200:
                    st.success(f"Post '{response['title']['rendered']}' updated successfully!")
                else:
                    st.error(f"Error: {response}")
        else:
            st.info("No posts available for update.")

    elif menu == "Delete":
        status_code, posts = read_posts()
        if status_code == 200:
            post_id = st.selectbox("Select Post to Delete", [post['id'] for post in posts])
            if st.button("Delete Post"):
                status_code, response = delete_post(post_id)
                if status_code == 200:
                    st.success("Post deleted successfully!")
                else:
                    st.error(f"Error: {response}")
        else:
            st.info("No posts available for deletion.")
