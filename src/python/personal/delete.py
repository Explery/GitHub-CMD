import requests

# Replace these with your own values
username = "YourUsername"
repository_name = "YourRepositoryName"
personal_access_token = "YourPersonalAccessToken"

def main():
    # Define the API endpoint for deleting a repository
    api_url = f"https://api.github.com/repos/{username}/{repository_name}"

    # Set the headers with your personal access token
    headers = {
        "Authorization": f"token {personal_access_token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Send a DELETE request to delete the repository
    response = requests.delete(api_url, headers=headers)

    # Check the response status code
    if response.status_code == 204:
        print(f"Repository '{repository_name}' has been deleted successfully.")
    elif response.status_code == 404:
        print(f"Repository '{repository_name}' not found.")
    else:
        print(f"Failed to delete repository '{repository_name}'. Status code: {response.status_code}")
        print(response.text)

main()