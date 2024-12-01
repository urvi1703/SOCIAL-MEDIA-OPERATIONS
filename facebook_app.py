import os
from dotenv import load_dotenv

# Load environment variables from fb.env file
load_dotenv(dotenv_path='fb.env')

# Now you can access your environment variables
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
PAGE_ID = os.getenv('PAGE_ID')

# Check if access token and page ID are loaded correctly
if not ACCESS_TOKEN or not PAGE_ID:
    print("Error: ACCESS_TOKEN or PAGE_ID not found in the environment variables.")
    exit(1)

# Base URL for Facebook API
BASE_URL = f"https://graph.facebook.com/v17.0/{PAGE_ID}"

# Function to create a post with text, image, or video
def create_post():
    print("Choose the type of post you want to create:")
    print("1. Text Post")
    print("2. Post with Image")
    print("3. Post with Video")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        # Text post
        message = input("Enter the message you want to post: ")
        url = f"{BASE_URL}/feed"
        params = {
            'message': message,
            'access_token': ACCESS_TOKEN
        }
        response = requests.post(url, params=params)
        if response.status_code != 200:
            print("Error:", response.json())
        else:
            print("Post Created Successfully:", response.json())

    elif choice == "2":
        # Image post
        image_path = input("Enter the full path of the image file: ")
        caption = input("Enter a caption for the image: ")
        url = f"{BASE_URL}/photos"
        params = {
            'caption': caption,
            'access_token': ACCESS_TOKEN
        }
        with open(image_path, 'rb') as image_file:
            files = {'source': image_file}
            response = requests.post(url, params=params, files=files)
            if response.status_code != 200:
                print("Error:", response.json())
            else:
                print("Image Post Created Successfully:", response.json())

    elif choice == "3":
        # Video post
        video_path = input("Enter the full path of the video file: ")
        description = input("Enter a description for the video: ")
        url = f"{BASE_URL}/videos"
        params = {
            'description': description,
            'access_token': ACCESS_TOKEN
        }
        with open(video_path, 'rb') as video_file:
            files = {'source': video_file}
            response = requests.post(url, params=params, files=files)
            if response.status_code != 200:
                print("Error:", response.json())
            else:
                print("Video Post Created Successfully:", response.json())

    else:
        print("Invalid choice. Returning to the main menu.")
        return

# Function to read posts
def read_posts():
    url = f"{BASE_URL}/posts"
    params = {'access_token': ACCESS_TOKEN}
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("Error:", response.json())
    else:
        print("Read Posts:", response.json())

# Function to update a post
def update_post():
    post_id = input("Enter the Post ID you want to update: ")
    new_message = input("Enter the new message: ")
    url = f"https://graph.facebook.com/{post_id}"
    params = {
        'message': new_message,
        'access_token': ACCESS_TOKEN
    }
    response = requests.post(url, params=params)
    if response.status_code != 200:
        print("Error:", response.json())
    else:
        print("Post Updated Successfully:", response.json())

# Function to delete a post
def delete_post():
    post_id = input("Enter the Post ID you want to delete: ")
    url = f"https://graph.facebook.com/{post_id}"
    params = {'access_token': ACCESS_TOKEN}
    response = requests.delete(url, params=params)
    if response.status_code != 200:
        print("Error:", response.json())
    else:
        print("Post Deleted Successfully:", response.json())

# Main menu for user interaction
def main():
    while True:
        print("\nChoose an operation:")
        print("1. Create a Post")
        print("2. Read Posts")
        print("3. Update a Post")
        print("4. Delete a Post")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            create_post()
        elif choice == "2":
            read_posts()
        elif choice == "3":
            update_post()
        elif choice == "4":
            delete_post()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main menu function
if __name__ == "__main__":
    main()
