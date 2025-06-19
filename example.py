import requests
import json
import os

api_key = os.environ.get('api_key')

url = f'https://api.nofiltergpt.com/v1/chat/completions?api_key={api_key}'

data = {
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello! Can you help me with something?"}
    ],
    "temperature": 0.7,
    "max_tokens": 150,
    "top_p": 1
}

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code != 200:
    print(f"Error: {response.status_code}")
else:
    print(response.json())
