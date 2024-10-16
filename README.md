# GoForGreen
## Overview
What is GoForGreen?  
GoForGreen (GFG) is a python script that checks if you have commited today on github so that your commit history timeline looks as green as possibe. Because thats all that matters, right?  
This script is meant to be automatically run on startup as a reminder, but that is entirely optional.
## Installation
These instructions are designed for linux. If you use windows, just clone the github repo as usual and you can make it auto execute yourself.  

Step 1: Curl main.py and GFGconfig.txt  
```
sudo curl -L -H https://raw.githubusercontent.com/Its-Rolo/GoForGreen/main/main.py -o /usr/local/bin/GoForGreen
sudo curl -L -H https://raw.githubusercontent.com/Its-Rolo/GoForGreen/main/GFGconfig.txt -o /usr/local/bin/GFGconfig.txt
sudo chmod a+rx /usr/local/bin/GoForGreen.py
```

Step 2: Edit GFGconfig.txt  
You should replace *username* with your github username,  
and replace *token* with one of your github personal access token(s). It does not need any special permissions.  

Step 3: Optionally make it execute on startup  
This step differs heavily based on DE/WM, but in hyprland for example add the following line to hyprland.conf:
```
exec-once = /usr/local/bin/GoForGreen.py
```
