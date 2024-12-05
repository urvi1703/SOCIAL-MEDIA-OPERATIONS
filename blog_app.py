import streamlit as st

# Initialize an in-memory database
if "blog_posts" not in st.session_state:
    st.session_state.blog_posts = {}

# Functions for CRUD operations
def create_post(title, content):
    st.session_state.blog_posts[title] = content

def read_posts():
    return st.session_state.blog_posts

def update_post(old_title, new_title, new_content):
    if old_title in st.session_state.blog_posts:
        st.session_state.blog_posts.pop(old_title)
        st.session_state.blog_posts[new_title] = new_content

def delete_post(title):
    if title in st.session_state.blog_posts:
        st.session_state.blog_posts.pop(title)

# Streamlit UI
st.title("Simple Blog App - CRUD Operations")

# Sidebar for navigation
menu = st.sidebar.selectbox("Menu", ["Create", "Read", "Update", "Delete"])

# Create Post
if menu == "Create":
    st.subheader("Create a New Blog Post")
    title = st.text_input("Post Title")
    content = st.text_area("Post Content")
    if st.button("Create"):
        if title and content:
            create_post(title, content)
            st.success(f"Post '{title}' created successfully!")
        else:
            st.error("Title and content cannot be empty!")

# Read Posts
elif menu == "Read":
    st.subheader("View Blog Posts")
    posts = read_posts()
    if posts:
        for title, content in posts.items():
            st.markdown(f"### {title}")
            st.write(content)
            st.markdown("---")
    else:
        st.info("No posts available.")

# Update Post
elif menu == "Update":
    st.subheader("Update an Existing Blog Post")
    posts = read_posts()
    if posts:
        old_title = st.selectbox("Select Post to Update", list(posts.keys()))
        new_title = st.text_input("New Title", old_title)
        new_content = st.text_area("New Content", posts[old_title])
        if st.button("Update"):
            if new_title and new_content:
                update_post(old_title, new_title, new_content)
                st.success(f"Post '{old_title}' updated to '{new_title}' successfully!")
            else:
                st.error("Title and content cannot be empty!")
    else:
        st.info("No posts available to update.")

# Delete Post
elif menu == "Delete":
    st.subheader("Delete a Blog Post")
    posts = read_posts()
    if posts:
        title = st.selectbox("Select Post to Delete", list(posts.keys()))
        if st.button("Delete"):
            delete_post(title)
            st.success(f"Post '{title}' deleted successfully!")
    else:
        st.info("No posts available to delete.")
