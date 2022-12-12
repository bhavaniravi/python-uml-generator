from github import Github
import os
import base64
import json
import requests
import pyimgur

from base64 import b64encode

ACCESS_TOKEN=os.getenv('ACCESS_TOKEN')
REPO_ID=os.getenv('REPO_ID')
PR_ID=os.getenv('PR_ID')
IMGUR_CLIENT_ID=os.getenv('IMGUR_CLIENT_ID')
IMGUR_API_KEY=os.getenv('IMGUR_API_KEY')
FILE_PATH=os.getenv('FILE_PATH')

g = Github(ACCESS_TOKEN)
repo = g.get_repo(REPO_ID)
pr = repo.get_pull(PR_ID)


def upload_image_get_link():
    # headers = {"Authorization": f"Client-ID {IMGUR_CLIENT_ID}"}
    # api_key = IMGUR_API_KEY

    # url = "http://api.imgur.com/3/upload.json"
    # with open(FILE_PATH, 'rb') as f:
    #     response = requests.post(
    #         url, 
    #         headers = headers,
    #         data = {
    #             'key': api_key, 
    #             'image': b64encode(f.read()),
    #             'type': 'base64',
    #             'name': f'{pr.head.sha}.png',
    #             'title': 'Picture no. 1'
    #         }
    #     )
    #     print (response.json())

    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH, title="Uploaded with PyImgur", url={pr.head.sha})
    return uploaded_image.link

link = upload_image_get_link()
# # Create a new review comment for the pull request
comment = pr.create_issue_comment(body=f"![]({link})", commit_id=commit_id, path=file_path, position=1)