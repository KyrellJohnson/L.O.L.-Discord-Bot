# League Of Legends Discord Bot

A discord bot used to interact with the Riot Games API to provide live stats, summoner info, etc. to servers with this bot added.

## How to use

### Setup on the Discord Developer Portal
- Create a Discord Developer Account at (https://discord.com/developers/applications)
- Create a new application and create a bot with elevated permissions
- Take note of your bots token as that will be needed later

### Setup on the Riot Games Portal
- Create a riot games developer account here (https://developer.riotgames.com/)
- See [here](https://developer.riotgames.com/apis) for API Reference
- Login to the dashboard and generate a new API Token
![image](https://user-images.githubusercontent.com/22106727/129656206-0ceee80e-258f-432e-9489-fe6aeb52e1df.png)

### Setting up the Pyhton Environment
- Include the following libraries to your Python environment
```
pip install -U discord.py
pip install riotwatcher
```
- In the code you will want to change line 5 and 6 with your tokens that you recieved in the discord and riot games developer portal
```
DISCORD_TOKEN = 'MY_BOT_TOKEN'
RIOT_GAMES_TOKEN = 'MY_API_KEY'
```
```diff
- IN A PRODUCTION ENVIRONMENT NEVER STORE ACTUAL TOKEN/API KEYS IN THIS FILE -
```

## Final Steps
- Go to the discord devloper portal and create a redirect using the ***OAuth2 URL Generator***
- After that using this link you can add this bot to a server you currently manage or create a new one for testing purposes
- Run your .py file and you have now created your own discord bot.

# Current Features
- Display the current rank of a player using: !rank playername
- More features to be added in future revisions...
