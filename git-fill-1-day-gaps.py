import requests

API_URL = "https://api.github.com"

# Note: this is a one day token, so it will expire 06/10/2023
# TODO: get token as program argument
AUTH_TOKEN = "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"


response = requests.get(API_URL + "/user", auth=("token", AUTH_TOKEN))
if (200 == response.status_code):
    print(response.json())
