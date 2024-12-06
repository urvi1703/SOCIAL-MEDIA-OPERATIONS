# -*- coding: utf-8 -*-
import requests
import streamlit as st
import time

# Replace with your bot's token and channel ID
BOT_TOKEN = "bot_token" #In GitHub Secret due to privacy issue
CHANNEL_ID = "1313061857157713963"
BASE_URL = "https://discord.com/api/v10"

# Headers for bot authentication
headers = {
    "Authorization": f"Bot {BOT_TOKEN}",
    "Content-Type": "application/json"
}

# Send a message to the Discord channel
def send_message(message):
    url = f"{BASE_URL}/channels/{CHANNEL_ID}/messages"
    response = requests.post(url, headers=headers, json=message)
    return response

# Read messages from a Discord channel (fetch the last 10 messages)
def fetch_messages():
    url = f"{BASE_URL}/channels/{CHANNEL_ID}/messages"
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else []

# Update a message
def update_message(message_id, new_content):
    url = f"{BASE_URL}/channels/{CHANNEL_ID}/messages/{message_id}"
    data = {
        "content": new_content
    }
    response = requests.patch(url, headers=headers, json=data)
    return response

# Delete a message
def delete_message(message_id):
    url = f"{BASE_URL}/channels/{CHANNEL_ID}/messages/{message_id}"
    response = requests.delete(url, headers=headers)
    return response

# Streamlit interface for interacting with Discord
def main():
    st.write("Welcome to Discord Operations!")

    action = st.selectbox("Choose an action", ["Send a Message", "Read Messages", "Update a Message", "Delete a Message"])

    if action == "Send a Message":
        # Add functionality to send a message to a Discord channel
        message_content = st.text_input("Enter your message:")
        if st.button("Send Message"):
            message = {"content": message_content}
            response = send_message(message)
            if response.status_code == 200:
                st.success("Message sent successfully!")
            else:
                st.error(f"Failed to send message. Status code: {response.status_code}")

    elif action == "Read Messages":
        # Add functionality to fetch messages from a Discord channel
        if st.button("Fetch Messages"):
            messages = fetch_messages()
            if messages:
                st.write("Messages in the channel:")
                for msg in messages:
                    st.write(f"Message ID: {msg['id']} | {msg['content']}")
            else:
                st.write("No messages found or failed to fetch messages.")

    elif action == "Update a Message":
        # Add functionality to update an existing message in a Discord channel
        message_id = st.text_input("Enter Message ID to update:")
        updated_message = st.text_input("Enter the updated message:")
        if st.button("Update Message"):
            response = update_message(message_id, updated_message)
            if response.status_code == 200:
                st.success(f"Message {message_id} updated successfully!")
            else:
                st.error(f"Failed to update message. Status code: {response.status_code}")

    elif action == "Delete a Message":
        # Add functionality to delete a message from a Discord channel
        message_id = st.text_input("Enter Message ID to delete:")
        if st.button("Delete Message"):
            response = delete_message(message_id)
            if response.status_code == 204:
                st.success(f"Message {message_id} deleted successfully!")
            else:
                st.error(f"Failed to delete message. Status code: {response.status_code}")

if __name__ == "__main__":
    main()
                
