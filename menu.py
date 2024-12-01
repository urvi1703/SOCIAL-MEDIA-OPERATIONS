# menu.py
import streamlit as st

def main():
    st.title("Social Media CRUD Operations")
    
    # Add a selectbox to choose between Facebook or YouTube
    app_selection = st.selectbox("Select a platform", ["Facebook", "YouTube"])
    
    if app_selection == "Facebook":
        # Import Facebook CRUD operations
        import facebook_crud
        facebook_crud.run()
    elif app_selection == "YouTube":
        # Import YouTube CRUD operations
        import youtube_crud
        youtube_crud.run()

if __name__ == "__main__":
    main()
