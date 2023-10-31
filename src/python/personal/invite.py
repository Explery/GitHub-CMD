import requests

# Replace these variables with your own values
github_username = "your_username"
github_repository = "your_repository"
invitee_username = "username_to_invite"
access_token = "your_personal_access_token"

def main():
    # Create the invitation URL
    invitation_url = f"https://api.github.com/repos/{github_username}/{github_repository}/collaborators/{invitee_username}"

    # Set up the headers with the access token
    headers = {
        "Authorization": f"token {access_token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Send the invitation
    response = requests.put(invitation_url, headers=headers)

    if response.status_code == 204:
        print(f"Invitation sent successfully to {invitee_username}.")
    else:
        print(f"Failed to send invitation. Status code: {response.status_code}")
        print(f"Response content: {response.content.decode()}")

main()