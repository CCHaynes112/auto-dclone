# Auto Dclone

Python app that automatically puts your character in a game when dclone is close to spawning.

This app is a very early WIP, so it's not very robust. It's also not very configurable. Next major step is to add a GUI.

 If you have any suggestions, please feel free to open an issue.

<a href="https://diablo2.io/dclonetracker.php">Data courtesy of diablo2.io</a>

diablo2.io is a great resource for all diablo 2 players. Highly recommend checking it out!

## Getting Started

* git clone the app
* cd into the app
* run `pip install -r requirements.txt`
* create a `config.py` file in the src directory
* add the following to the `config.py` file
```python
# Twilio account info
TWILIO_ACCOUNT_SID = '<TWILIO_ACCOUNT_SID>'
TWILIO_AUTH_TOKEN = '<TWILIO_AUTH_TOKEN>'

# Notification settings
NOTIFICATION_ENABLED = True
SMS_FROM_NUMBER = '<TWILIO_PHONE_NUMBER>'
SMS_TO_NUMBER = '<YOUR_PHONE_NUMBER>'
SMS_BODY = "Dclone is spawning! Go get him!"

# This is the api that we are polling
URL = "https://diablo2.io/dclone_api.php"
REGION = None # 1 = America, 2 = Europe, 3 = Asia
LADDER = None # 1 = ladder, 2 = non-ladder
HARDCORE = None # 1 = hardcore, 2 = softcore

# Path to diablo 2 launcher
LAUNCHER_PATH = "C:/Program Files (x86)/Battle.net/Battle.net Launcher.exe"
```
* customize the `config.py` file to your liking
* take a screenshot of the character from the character list on the right side of the character selection screen. After you've taken the screenshot, add it to the `assets/img` directory and name it `character_name.png`
* run `python auto_dclone.py`

## Built With

* Python
* PyAutoGUI

## Authors

* **Curtis Haynes**