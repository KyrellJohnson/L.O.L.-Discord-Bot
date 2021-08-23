from gc import collect
from pymongo import MongoClient
import pymongo
import pprint
import os


from requests.api import post

def connectToDB(DB_STRING):
    DATABASE_STRING = DB_STRING
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = DATABASE_STRING

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)
    
    
    print(client)
    """ pprint.pprint(collection.find_one())
    post = {"_discordUser" : "John",
            "_summonerName" : "K"
            }

    collection.insert_one(post).inserted_id
    pprint.pprint(collection.find_one({"_id" : "611c6b78d97c297a9ca07510"})) """
    return client

def addSummonerToUser(summonerName, discordUser, db_client):
    
    #get db name
    db = db_client['LeagueChan']
    collection = db['users']

    #check if user already has an assigned summoner name
    if(collection.count({"_discordUser" : discordUser}) > 1):
        #do not add to DB
        #tell user there discord acct is attached to summoner name
        return 'User: ' + discordUser + " already has a summoner name assigned to their account." + "\n" + "Use command [!update summonerName] to assign a new summoner name."      
    else:
        post = {"_discordUser" : discordUser,
                "_summonerName" : summonerName
                }
        collection.insert_one(post)

    
    
def updateSummonerNameToUser():
    "TODO"

def removeSummonerNameFromUser():
    "TODO"

def getSummonerNameOfUser():
    "TODO"
