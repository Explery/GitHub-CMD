import requests

# Replace these with your own values
username = "YourUsername"
repository_name = "YourRepositoryName"
personal_access_token = "YourPersonalAccessToken"

def main():
    # Define the API endpoint for creating a repository
    api_url = f"https://api.github.com/user/repos"

    # Set the headers with your personal access token
    headers = {
        "Authorization": f"token {personal_access_token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Create a dictionary with the repository name and other optional parameters
    data = {
        "name": repository_name,
        "auto_init": True,  # Initialize with a README.md file
        "private": True, # This is visible of repository
        # You can add more parameters here, such as description, private, etc.
    }

    # Send a POST request to create the repository
    response = requests.post(api_url, headers=headers, json=data)

    # Check the response status code
    if response.status_code == 201:
        print(f"Repository '{repository_name}' has been created successfully.")
    else:
        print(f"Failed to create repository '{repository_name}'. Status code: {response.status_code}")
        print(response.text)

main()