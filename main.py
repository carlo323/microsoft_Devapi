import requests
import json

url = "https://api.github.com/user/repos"

headers = {
    "Authorization": "Bearer " + access_token,
    "Content-Type": "application/json"
}

payload = {
    "name": "new-repo",
    "description": "This is a new repository",
    "private": False
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

print(response.status_code)
