import requests
from datetime import datetime
from plyer import notification
import os

# Check if the file exists
if os.path.exists("./GFGconfig.txt"):
    with open("./GFGconfig.txt", "r") as f:
        username = f.readline().strip()  # Read and strip whitespace
        token = f.readline().strip()
else:
    print("The file GFGconfig.txt does not exist.")
    exit()

url = f"https://api.github.com/users/{username}/events"

headers = {
    "Authorization": f"token {token}" 
}

response = requests.get(url, headers=headers)


if response.status_code == 200:
    events = response.json()
    committed_today = False 

    for event in events:
        if event["type"] == "PushEvent":
            event_date = datetime.strptime(event["created_at"], "%Y-%m-%dT%H:%M:%SZ").date()
            if event_date == datetime.today().date():
                committed_today = True
                break 


    if committed_today:
        notification.notify(
            title="GoForGreen Commit Check",
            message=f"You have committed today in {event['repo']['name']}!",
            app_name="GitHub Notifier",
            timeout=5
        )
    else:
        notification.notify(
            title="GoForGreen Commit Check",
            message="You have not committed today :(",
            app_name="GitHub Notifier",
            timeout=5  # Duration the notification stays on screen
        )
else:
    print(f"Failed to fetch events: {response.status_code}")
