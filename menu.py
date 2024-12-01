import streamlit as st

# Main function that controls the app flow
def main():
    # Set the title of the app
    st.title("Social Media CRUD Operations")
    
    # Add a selectbox for platform selection
    app_selection = st.selectbox("Select a platform", ["Facebook", "YouTube"])
    
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

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
