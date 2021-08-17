from riotwatcher import LolWatcher, ApiError
from dotenv import load_dotenv
import os

def findRank(summonerName, region):
    #Load environmental variable file
    load_dotenv()

    #Get API Token
    RIOT_GAMES_TOKEN = os.getenv('RIOT_API_KEY')


    lol_watcher = LolWatcher(RIOT_GAMES_TOKEN)

    my_region = region

    me = lol_watcher.summoner.by_name(my_region, summonerName)

    my_ranked_stats = lol_watcher.league.by_summoner(my_region, me['id'])
    #print((my_ranked_stats))
    summonerTier = ([a_dict['tier'] for a_dict in my_ranked_stats])
    summonerRank = ([a_dict['rank'] for a_dict in my_ranked_stats])

    summonerRanker = str(summonerTier).lstrip("['").rstrip("']") + " " + str(summonerRank).lstrip("['").rstrip("']")

    return summonerRanker