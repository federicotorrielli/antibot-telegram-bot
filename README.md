# Antibot and antiflood bot for telegram / AKA NeeggaBot
This is an anti flood system for telegram messenger that i created for people who need anti flood protection in their groups by other users.
It also bans every new bot that tries to join the group or is invited to the group: be careful!
This bot was originally a fork from another project, but since I added new functions and the project is now completely different, I created his own repository.

# How can i add my bot token?
Get your bot token from BotFather then open the file antiflood_config.py and put it in the `token` field

## Installation
You already know the drill: `pip install -r requirements.txt` to install the necessary requirements, then just hop on a server and do:
#### Linux and distros
`python3 antiflood.py`
#### That vomithole called "Windows"
`python antiflood.py`
#### Heroku
1) Create an heroku project
2) Commit this repo and push the project with the buildpack "heroku/python"
3) Hop again on your terminal and do `heroku ps:scale worker=1`
4) Profit!

# Guidelines
You can contribute to the project as long as:
1) You love monke
2) You regret to be human and want to embrace anarcho-privitivism
3) You are a real pythonic dude
