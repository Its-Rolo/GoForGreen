# GoForGreen
## Overview
What is GoForGreen?  
GoForGreen (GFG) is a python script that checks if you have commited today on github so that your commit history timeline looks as green as possible. Because thats all that matters, right?  
This script is meant to be automatically run on startup as a reminder, but that is entirely optional.  

Please note that the script uses absolute linux file structure paths and the installation guide is also for linux!
## Installation
Step 1: Curl main.py and GFGconfig.txt  
```
sudo curl -L -o /usr/local/bin/GoForGreen https://raw.githubusercontent.com/Its-Rolo/GoForGreen/main/main.py
sudo curl -L -o /usr/local/bin/GFGconfig.txt https://raw.githubusercontent.com/Its-Rolo/GoForGreen/main/GFGconfig.txt
sudo chmod a+rx /usr/local/bin/GoForGreen
```

Step 2: Edit GFGconfig.txt  
You should replace *username* with your github username,  
and replace *token* with one of your github personal access token(s). It does not need any special permissions.  

Step 3: Optionally make it execute on startup  
This step differs heavily based on DE/WM, but in hyprland for example add the following line to hyprland.conf:
```
exec-once = /usr/local/bin/GoForGreen.py
```

## Updating
To update GoForGreen to the latest version on this repo, simply run the following command:
```
sudo rm /usr/local/bin/GoForGreen.py
sudo curl -L -o /usr/local/bin/GoForGreen https://raw.githubusercontent.com/Its-Rolo/GoForGreen/main/main.py
sudo chmod a+rx /usr/local/bin/GoForGreen
```

## Uninstallation
To uninstall GoForGreen, simply run the following command:
```
sudo rm /usr/local/bin/GoForGreen
sudo rm /usr/local/bin/GFGconfig.txt
```
