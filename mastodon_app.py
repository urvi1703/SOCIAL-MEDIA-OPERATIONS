from mastodon import Mastodon
import streamlit as st

# Mastodon API credentials
INSTANCE_URL = "https://mastodon.social"  # Replace with your Mastodon instance URL
ACCESS_TOKEN = "your-access-token-here"  # Replace with your access token

# Initialize the Mastodon client
mastodon = Mastodon(
    access_token=ACCESS_TOKEN,
    api_base_url=INSTANCE_URL
)

# CRUD Operations
def create_toot(content):
    """Create a new toot (post)."""
    toot = mastodon.status_post(content)
    return toot

def read_toots():
    """Read recent toots from your account."""
    toots = mastodon.timeline_home(limit=10)  # Fetch the 10 most recent toots
    return toots

def update_toot(toot_id, new_content):
    """Mastodon doesn't support editing toots, but you can delete and repost."""
    mastodon.status_delete(toot_id)
    updated_toot = create_toot(new_content)
    return updated_toot

def delete_toot(toot_id):
    """Delete a toot."""
    mastodon.status_delete(toot_id)
    return True

# Streamlit UI
def main():
    st.title("Mastodon CRUD Operations")
    
    # Sidebar menu
    menu = st.sidebar.radio("Menu", ["Create", "Read", "Delete"])
    
    if menu == "Create":
        st.subheader("Create a New Toot")
        content = st.text_area("Enter toot content")
        if st.button("Post Toot"):
            if content:
                toot = create_toot(content)
                st.success(f"Toot created successfully! ID: {toot['id']}")
            else:
                st.warning("Content cannot be empty.")
    
    elif menu == "Read":
        st.subheader("Read Recent Toots")
        toots = read_toots()
        if toots:
            for toot in toots:
                st.markdown(f"**{toot['account']['display_name']}**: {toot['content']}")
                st.write(f"Toot ID: {toot['id']}")
                st.markdown("---")
        else:
            st.info("No toots available.")
    
    elif menu == "Delete":
        st.subheader("Delete a Toot")
        toots = read_toots()
        toot_ids = [toot['id'] for toot in toots]
        selected_toot = st.selectbox("Select a toot to delete", toot_ids)
        if st.button("Delete Toot"):
            delete_toot(selected_toot)
            st.success(f"Toot with ID {selected_toot} deleted successfully!")

# Run the app
if __name__ == "__main__":
    main()
