# from git import Repo
from github import Github
from github import Auth


# Note: this is a one day token, so it will expire 06/10/2023
auth = Auth.Token("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")

# First create a Github instance:

# Public Web Github
g = Github(auth=auth)

# Github Enterprise with custom hostname
g = Github(base_url="https://{hostname}/api/v3", auth=auth)

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)

# To close connections after use
g.close()
