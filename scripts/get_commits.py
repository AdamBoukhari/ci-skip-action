import requests
import os
import sys

REPO = os.environ["GITHUB_REPOSITORY"]
TOKEN = os.environ["GITHUB_TOKEN"]
BEFORE_SHA = sys.argv[1]
AFTER_SHA = sys.argv[2]

API_URL = f"https://api.github.com/repos/{REPO}/compare/{BEFORE_SHA}...{AFTER_SHA}"

headers = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

response = requests.get(API_URL, headers=headers)

if response.status_code != 200:
    print(f"Failed to fetch commits: {response.status_code}")
    exit(1)

data = response.json()
commit_messages = [commit["commit"]["message"] for commit in data["commits"]]
print("\n".join(commit_messages).replace("\n", "%0A"))
