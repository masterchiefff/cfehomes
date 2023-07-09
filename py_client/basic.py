import requests

endpoint = "http://127.0.0.1:8000/api"

try:
    git_response = requests.get(endpoint, params={"abc": 123}, json={"query": "Hello world"})
    git_response.raise_for_status()  # Raise an exception for non-2xx status codes

    response_data = git_response.json()
    print(response_data)
except requests.exceptions.RequestException as e:
    print("An error occurred:", e)