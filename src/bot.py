from asyncio.windows_events import NULL
from riotwatcher import LolWatcher, ApiError
import discord
from databaseHandler import *
from dotenv import load_dotenv
import os

 
def main():

    #Load environmental variable file
    load_dotenv()

    #Get User Tokens / Keys
    DISCORD_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
    RIOT_GAMES_TOKEN = os.getenv('RIOT_API_KEY')
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
            cmd = readMessage(message.content)
            
            if(cmd != NULL):
                await message.channel.send(cmd)

    client.run(DISCORD_TOKEN)
            

    def readMessage(msg):
        returnMSG = NULL
        #check if command is a rank command
        if(msg.startswith("!rank ")):

            #strip out !rank
            returnMSG = msg.lstrip('!rank')
            #remove leading whitespace
            returnMSG = returnMSG.lstrip()
            #return returnMSG

        #get rank from input string
        if(returnMSG):
            returnMSG = getLOLRank(returnMSG)

        return returnMSG
        
    def getLOLRank(summonerName):
        lol_watcher = LolWatcher(RIOT_GAMES_TOKEN)

        my_region = 'na1'

        me = lol_watcher.summoner.by_name(my_region, summonerName)

        my_ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])
        print((my_ranked_stats))
        summonerTier = ([a_dict['tier'] for a_dict in my_ranked_stats])
        summonerRank = ([a_dict['rank'] for a_dict in my_ranked_stats])

        summonerRanker = str(summonerTier).lstrip("['").rstrip("']") + " " + str(summonerRank).lstrip("['").rstrip("']")

        return (summonerRanker)
        

    

if __name__ == "__main__":
    main()