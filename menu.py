# menu.py
import streamlit as st

def main():
    st.title("Social Media CRUD Operations")
    
    # Add a selectbox to choose between Facebook or YouTube
    app_selection = st.selectbox("Select a platform", ["Facebook", "YouTube"])
    
    if app_selection == "Facebook":
        # Import Facebook CRUD operations (make sure to have facebook_crud.py)
        import facebook_crud
        facebook_crud.run()  # This calls the run function in facebook_crud.py
    elif app_selection == "YouTube":
        # Import YouTube CRUD operations (your youtube_app.py)
        import youtube_app
        youtube_app.main()  # This calls the main function in youtube_app.py

if __name__ == "__main__":
    main()
