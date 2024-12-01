import streamlit as st
import requests

# Function to get Facebook data using Graph API
def get_facebook_data(access_token, page_id):
    url = f"https://graph.facebook.com/{page_id}?fields=id,name,about,posts&access_token={access_token}"
    response = requests.get(url)
    data = response.json()
    return data

# Function to update Facebook page description (Simulating Update)
def update_facebook_page(access_token, page_id, new_description):
    url = f"https://graph.facebook.com/{page_id}"
    payload = {
        'about': new_description,
        'access_token': access_token
    }
    response = requests.post(url, data=payload)
    data = response.json()
    return data

# Function to delete a post from Facebook page (Simulating Delete)
def delete_facebook_post(access_token, post_id):
    url = f"https://graph.facebook.com/{post_id}?access_token={access_token}"
    response = requests.delete(url)
    data = response.json()
    return data

# Streamlit App
def main():
    st.title("Facebook Data Viewer & CRUD Operations")
    
    st.markdown("""
    This Streamlit app fetches public data from a Facebook page using the Graph API. 
    You can also perform basic CRUD operations like retrieving page data, updating the description, 
    and deleting posts.
    """)

    # User input for access token and page ID
    access_token = st.text_input("Enter your Facebook Access Token", type="password")
    page_id = st.text_input("Enter the Facebook Page ID")

    # CRUD Options
    operation = st.selectbox("Select an Operation", ["Get Page Data", "Update Page Description", "Delete Post"])

    # Handling 'Get Page Data'
    if operation == "Get Page Data" and st.button("Get Facebook Data"):
        if access_token and page_id:
            with st.spinner("Fetching data from Facebook..."):
                data = get_facebook_data(access_token, page_id)
                
                if 'error' in data:
                    st.error(f"Error: {data['error']['message']}")
                else:
                    st.subheader(f"Page Information: {data['name']}")
                    st.write(f"Page ID: {data['id']}")
                    if 'about' in data:
                        st.write(f"About: {data['about']}")
                    
                    if 'posts' in data:
                        st.subheader("Latest Posts:")
                        for post in data['posts']['data']:
                            st.write(post.get("message", "No message available"))
                            st.write(f"Posted on: {post.get('created_time', 'Unknown time')}")
                            st.markdown("---")
        else:
            st.warning("Please provide both access token and page ID.")
    
    # Handling 'Update Page Description'
    elif operation == "Update Page Description" and st.button("Update Description"):
        if access_token and page_id:
            new_description = st.text_area("Enter New Description")
            if new_description:
                with st.spinner("Updating page description..."):
                    result = update_facebook_page(access_token, page_id, new_description)
                    if 'error' in result:
                        st.error(f"Error: {result['error']['message']}")
                    else:
                        st.success(f"Page description updated successfully!")
            else:
                st.warning("Please provide a new description.")
        else:
            st.warning("Please provide both access token and page ID.")
    
    # Handling 'Delete Post'
    elif operation == "Delete Post" and st.button("Delete Post"):
        if access_token and page_id:
            post_id = st.text_input("Enter Post ID to Delete")
            if post_id:
                with st.spinner("Deleting post..."):
                    result = delete_facebook_post(access_token, post_id)
                    if 'error' in result:
                        st.error(f"Error: {result['error']['message']}")
                    else:
                        st.success(f"Post deleted successfully!")
            else:
                st.warning("Please provide a post ID.")
        else:
            st.warning("Please provide both access token and page ID.")

if __name__ == "__main__":
    main()
