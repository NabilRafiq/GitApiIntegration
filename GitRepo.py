import requests
import json

GITHUB_API_BASE_URL = 'https://api.github.com/users/'
username = 'NabilRafiq'

# getting repos of user
repos='/repos'
header = {"Authorization": "Bearer AccessToken"}

respones = requests.get(
    url=f"{GITHUB_API_BASE_URL}{username}{repos}",
    headers=header
)

data = respones.json()
with open('repos_data.json', 'w') as file:
    json.dump(data, file,indent=3)
print(data)

##Create a Repo
GITHUB_API_BASE_URL = 'https://api.github.com/user/repos'
username = 'NabilRafiq'
name = input("Enter Repo Name ")
desc = input("Enter Repo Desc ")
new_repo_data = {
    'name': name,
    'description': desc,
    'homepage': 'https://github.com',
    'private': False,
    'has_issues': True,
    'has_projects': True,
    'has_wiki': True
}
headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': 'Bearer Access Token',
    'X-GitHub-Api-Version': '2022-11-28',
    'Content-Type': 'application/x-www-form-urlencoded',
        }

json_data = json.dumps(new_repo_data)
response = requests.post(url=GITHUB_API_BASE_URL, data=json_data, headers=headers)
if response.status_code == 201:
    print("Repository created successfully!")
else:
    print(f"Failed to create repository. Status code: {response.status_code}")
    print(response.json())