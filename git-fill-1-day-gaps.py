import requests

API_URL = "https://api.github.com"

# TODO: get new token
AUTH_TOKEN = "ghp_..."


response = requests.get(API_URL + "/user", auth=("token", AUTH_TOKEN))
if (200 == response.status_code):
    print(response.json())


def get_contributions():
    response = requests.get(API_URL + "/user", auth=("token", AUTH_TOKEN))
    if (200 == response.status_code):
        print(response.json())


# REST API might not have /contributions endpoint
# Although the GraphQL API allows to get such data
# https://docs.github.com/en/graphql/overview/explorer
