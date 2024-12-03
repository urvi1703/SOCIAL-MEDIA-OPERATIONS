import streamlit as st

# Main function that controls the app flow
def main():
    # Set the title of the app
    st.title("Social Media CRUD Operations")
    
    # Add a selectbox for platform selection
    app_selection = st.selectbox("Select a platform", ["Facebook", "YouTube", "Reddit", "Discord","Instagram"])
    
    if app_selection == "Facebook":
        # Facebook operations - import and call the appropriate function from facebook_app.py
        import facebook_app
        st.subheader("Facebook Operations")
        facebook_app.main()  # Ensure the main function in facebook_app is properly defined
    
    elif app_selection == "YouTube":
        # YouTube operations - import and call the appropriate function from youtube_app.py
        import youtube_app
        st.subheader("YouTube Operations")
        youtube_app.main()  # Ensure the main function in youtube_app is properly defined
    
    elif app_selection == "Reddit":
        # Reddit operations - import and call the appropriate function from reddit_app.py
        import app
        st.subheader("Reddit Operations")
        app.main()  # Ensure the main function in app.py is properly defined
    
    elif app_selection == "Discord":
        # Discord operations - import and call the appropriate function from discord_app.py
        import discord_app
        st.subheader("Discord Operations")
        discord_app.main()  # Ensure the main function in discord_app is properly defined
        
    elif app_selection == "Instagram":
        import instagram_app
        st.subheader("Instagram Operations")
        instagram_app.main()


# Run the main function when the script is executed
if __name__ == "__main__":
    main()
