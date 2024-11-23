import webbrowser
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json
import os
import time

# Define constants for the credentials file and scopes
CLIENT_SECRET_FILE = "/Users/apple/repos/SOCIAL-MEDIA-OPERATIONS/client_secret.json"
TOKEN_FILE = 'token.json'
SCOPES = ['https://www.googleapis.com/auth/youtube']

# Global variable for rate limiting
last_request_time = 0

# Initialize YouTube API client
def initialize_youtube():
    print("Initializing YouTube API client...")
    creds = load_credentials()
    youtube = build('youtube', 'v3', credentials=creds)
    print("YouTube API client initialized.")
    return youtube

# Load or get credentials with OAuth
def load_credentials():
    creds = None
    if os.path.exists(TOKEN_FILE):
        print("Loading credentials from token file...")
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
        print("Credentials loaded from token file.")
    else:
        print("No valid token found, starting OAuth flow...")
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
        creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
        print("New credentials obtained and saved to token file.")
    return creds

# Create (Upload) a video with rate limiting
def upload_video(file_path, title, description):
    youtube = initialize_youtube()
    print(f"Uploading video: {title}")
    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "tags": ["example", "CRUD"],
                "categoryId": "22"
            },
            "status": {
                "privacyStatus": "private"
            }
        },
        media_body=file_path
    )
    try:
        response = request.execute()
        print(f"Video uploaded successfully with ID: {response['id']}")
        # Display and open the YouTube page
        print(f"View the uploaded video here: https://www.youtube.com/watch?v={response['id']}")
        webbrowser.open(f"https://www.youtube.com/watch?v={response['id']}")
        return response['id']
    except HttpError as error:
        print(f"Error uploading video: {error}")
        return None


# Read (Retrieve) video details with rate limiting
def get_video_details(video_id):
    youtube = initialize_youtube()
    print(f"Retrieving details for video ID: {video_id}")
    request = youtube.videos().list(
        part="snippet,contentDetails,statistics",
        id=video_id
    )
    try:
        response = request.execute()
        print("Video Details:")
        print(json.dumps(response, indent=4))
        return response
    except HttpError as error:
        print(f"Error getting video details: {error}")
        return None

# Update video details with rate limiting
def update_video(video_id, new_title, new_description):
    youtube = initialize_youtube()
    print(f"Updating video ID: {video_id} with new title and description")
    request = youtube.videos().update(
        part="snippet",
        body={
            "id": video_id,
            "snippet": {
                "title": new_title,
                "description": new_description,
                "categoryId": "22"
            }
        }
    )
    try:
        response = request.execute()
        print(f"Video with ID {video_id} updated successfully.")
        # Display and open the YouTube page
        print(f"View the updated video here: https://www.youtube.com/watch?v={video_id}")
        webbrowser.open(f"https://www.youtube.com/watch?v={video_id}")
        return response
    except HttpError as error:
        print(f"Error updating video: {error}")
        return None


# Delete a video with rate limiting
def delete_video(video_id):
    youtube = initialize_youtube()
    print(f"Deleting video ID: {video_id}")
    request = youtube.videos().delete(id=video_id)
    try:
        request.execute()
        print(f"Video with ID {video_id} deleted successfully.")
    except HttpError as error:
        print(f"Error deleting video: {error}")

# Main function to demonstrate CRUD operations
def main():
    # Path to the video file
    file_path = "/Users/apple/repos/SOCIAL-MEDIA-OPERATIONS/video.mp4"
# Update this path
 # Replace with the path to your video file
    title = "Sample Upload Video"
    description = "This is a test upload video using the YouTube API"

    print("1. Creating/Uploading the video...")
    # 1. Create/Upload
    video_id = upload_video(file_path, title, description)
    if video_id:  # Only proceed if upload was successful
        print("\n2. Retrieving video details...")
        # 2. Read
        get_video_details(video_id)

        print("\n3. Updating video details...")
        # 3. Update
        new_title = "Updated Video Title"
        new_description = "This is the updated description for the video."
        update_video(video_id, new_title, new_description)

        print("\n4. Deleting the video...")
        # 4. Delete
        delete_video(video_id)

if __name__ == "__main__":
    main()