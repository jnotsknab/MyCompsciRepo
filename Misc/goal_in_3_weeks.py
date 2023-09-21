import os
import shutil
import time
import requests
from PIL import Image
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Previously defined functions
# create_folders, rename_files, and backup_folder

def download_file(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)
    print(f"Downloaded {url} to {save_path}")

def resize_image(image_path, output_path, size):
    img = Image.open(image_path)
    img_resized = img.resize(size)
    img_resized.save(output_path)
    print(f"Resized {image_path} and saved as {output_path}")

def send_email(to, subject, body, attachment_paths):
    try:
        # Set up credentials
        credentials = service_account.Credentials.from_service_account_file(
            'path/to/your/credentials.json', scopes=['https://www.googleapis.com/auth/gmail.send'])

        service = build('gmail', 'v1', credentials=credentials)

        message = MIMEMultipart()
        message['to'] = to
        message['subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        for attachment_path in attachment_paths:
            with open(attachment_path, 'rb') as file:
                img_data = file.read()

            image = MIMEImage(img_data)
            image.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(attachment_path)}"')
            message.attach(image)

        create_message = {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}
        send_message = (service.users().messages().send(userId="me", body=create_message).execute())
        print(F'sent message to {to} Message Id: {send_message["id"]}')
    except HttpError as error:
        print(F'An error occurred: {error}')
        send_message = None
    return send_message

# Customize these variables for your specific needs
# Base variables
# ...

# Download file variables
url = "https://www.example.com/file.jpg"
save_path = "/path/to/save/location/file.jpg"

# Resize image variables
image_path = save_path
output_path = "/path/to/save/location/resized_file.jpg"
size = (800, 800)

# Send email variables
to = "recipient@example.com"
subject = "Automated Email with Attachments"
body = "Here's an example email with attachments."
attachment_paths = [output_path]

# Execute functions
# ...

# Execute new functions
download_file(url, save_path)
resize_image(image_path, output_path, size)
send_email(to, subject, body, attachment_paths)