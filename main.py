#!/usr/bin/env python3

import requests
from datetime import datetime
from plyer import notification
import os
import time
import pytz  # Required for timezone handling

time.sleep(10)  # Wait for other services to run first.

# Check if the configuration file exists
config_path = "/usr/local/bin/GFGconfig.txt"
if os.path.exists(config_path):
    with open(config_path, "r") as f:
        username = f.readline().strip()  # Read and strip whitespace
        token = f.readline().strip()
else:
    print("The file GFGconfig.txt does not exist.")
    exit()

# Define your repository name here
repository_name = "Its-Rolo/GoForGreen"  # Update as needed

# Get today's date in EST
est_tz = pytz.timezone('America/New_York')
today_start = datetime.now(est_tz).date()
today_start_iso = f"{today_start}T00:00:00Z"

# Construct the API URL to fetch today's commits
url = f"https://api.github.com/repos/{repository_name}/commits?since={today_start_iso}"

headers = {
    "Authorization": f"token {token}"
}

# Make the request to GitHub API
response = requests.get(url, headers=headers)

if response.status_code == 200:
    commits = response.json()
    committed_today = len(commits) > 0

    if committed_today:
        commit_messages = [commit['commit']['message'] for commit in commits]
        notification.notify(
            title="GoForGreen Commit Check",
            message=f"You have committed today in {repository_name}!",
            app_name="GitHub Notifier",
            timeout=5
        )
    else:
        notification.notify(
            title="GoForGreen Commit Check",
            message="You have not committed today :(",
            app_name="GitHub Notifier",
            timeout=5
        )
else:
    print(f"Failed to fetch commits: {response.status_code}, {response.text}")
