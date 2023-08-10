import requests

# Replace these with your app's credentials
client_id = 'your-client-id'
client_secret = 'your-client-secret'
tenant_id = 'your-tenant-id'

url = f'https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token'
data = {
    'client_id': client_id,
    'scope': 'https://graph.microsoft.com/.default',
    'client_secret': client_secret,
    'grant_type': 'client_credentials',
}
response = requests.post(url, data=data)
response.raise_for_status()  # Raise exception if the request failed
access_token = response.json()['access_token']

url = 'https://graph.microsoft.com/v1.0/me/sendMail'
headers = {'Authorization': 'Bearer ' + access_token}
json = {
    "message": {
        "subject": "Hello from Python",
        "body": {
            "contentType": "Text",
            "content": "Hello, world!"
        },
        "toRecipients": [
            {
                "emailAddress": {
                    "address": "example@example.com"
                }
            }
        ]
    },
    "saveToSentItems": "true"
}
response = requests.post(url, headers=headers, json=json)
response.raise_for_status()  # Raise exception if the request failed
