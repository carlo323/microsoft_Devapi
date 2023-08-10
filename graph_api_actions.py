import requests
import json

url = "https://graph.microsoft.com/v1.0/users/{id}/calendar/events"

headers = {
    "Authorization": "Bearer " + access_token,
    "Content-Type": "application/json"
}
# Creating a calendar event
payload = {
    "subject": "Let's go for lunch",
    "body": {
        "contentType": "HTML",
        "content": "Does late morning work for you?"
    },
    "start": {
        "dateTime": "2022-01-01T12:00:00",
        "timeZone": "Pacific Standard Time"
    },
    "end": {
        "dateTime": "2022-01-01T14:00:00",
        "timeZone": "Pacific Standard Time"
    },
    "location":{
        "displayName":"Harry's Bar"
    },
    "attendees": [
        {
            "emailAddress": {
                "address":"example@example.com",
                "name":"John Doe"
            },
            "type": "required"
        }
    ]
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

print(response.status_code)


import requests

url = "https://graph.microsoft.com/v1.0/users/{id}"

headers = {"Authorization": "Bearer " + access_token}

response = requests.get(url, headers=headers)

print(response.json())



url = "https://graph.microsoft.com/v1.0/users/{id}"

headers = {
    "Authorization": "Bearer " + access_token,
    "Content-Type": "application/json"
}

payload = {
    "jobTitle": "New Job Title"
}

response = requests.patch(url, headers=headers, data=json.dumps(payload))

print(response.status_code)



url = "https://graph.microsoft.com/v1.0/users/{id}/messages"

headers = {"Authorization": "Bearer " + access_token}

response = requests.get(url, headers=headers)

print(response.json())

url = "https://graph.microsoft.com/v1.0/groups"

headers = {
    "Authorization": "Bearer " + access_token,
    "Content-Type": "application/json"
}

payload = {
    "displayName": "New Group",
    "mailEnabled": False,
    "mailNickname": "newgroup",
    "securityEnabled": True
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

print(response.status_code)
