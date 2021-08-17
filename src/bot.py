from asyncio.windows_events import NULL
import discord
from databaseHandler import *
from commandParser import *
from dotenv import load_dotenv
import os

 
def main():

    #Load environmental variable file
    load_dotenv()

    #Get User Tokens / Keys
    DISCORD_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
    DATABASE_STRING = os.getenv('DB_ACCESS_STRING')
    
    #connect to Database
    connectToDB(DATABASE_STRING)

    client = discord.Client()

    @client.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        
        #only check messages prefixed with ' ! '
        if message.content.startswith('!'):
            cmd = readCommand(message.content)
            
            if(cmd != NULL):
                await message.channel.send(cmd)

    client.run(DISCORD_TOKEN)

if __name__ == "__main__":
    main()