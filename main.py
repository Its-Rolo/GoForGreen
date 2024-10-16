#!/usr/bin/env python3

import requests
from datetime import datetime
from plyer import notification
import os
import time
import pytz

time.sleep(10)  # IMPORTANT!!!! Waits for other services to run first otherwise it will break

if os.path.exists("/usr/local/bin/GFGconfig.txt"):
    with open("/usr/local/bin/GFGconfig.txt", "r") as f:
        username = f.readline().strip()
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

    # Get today's local date
    today_local = datetime.now().date()

    for event in events:
        if event["type"] == "PushEvent":
            # Convert GitHub UTC time to local time
            event_date = datetime.strptime(event["created_at"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=pytz.utc).astimezone().date()

            # Check if the event happened today (local calendar date)
            if event_date == today_local:
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
