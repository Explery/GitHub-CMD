# This code made for delete repository in organization when it have too many
# I also make exclude for repository that need to keep too
import requests

# Your GitHub personal access token
token = ""

# The organization name
org_name = ""

# List of repository names to exclude from deletion
exclude_repos = [""]  # Add the names of the repositories you want to exclude

# Create a session with your access token
session = requests.Session()
session.headers.update({'Authorization': f'token {token}'})

# Get a list of all repositories in the organization
url = f'https://api.github.com/orgs/{org_name}/repos'
response = session.get(url)
repos = response.json()

# Loop through the repositories and delete them, excluding the specified ones
for repo in repos:
    repo_name = repo['name']
    if repo_name not in exclude_repos:
        delete_url = f'https://api.github.com/repos/{org_name}/{repo_name}'
        delete_response = session.delete(delete_url)
        if delete_response.status_code == 204:
            print(f"Deleted {repo_name}")
        else:
            print(f"Failed to delete {repo_name}. Status code: {delete_response.status_code}")
