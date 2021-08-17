from pymongo import MongoClient
import pymongo

def connectToDB(DB_STRING):
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = DB_STRING

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)
    print(client)

def addSummonerToUser():
    "TODO"
    
def updateSummonerNameToUser():
    "TODO"

def removeSummonerNameFromUser():
    "TODO"

def getSummonerNameOfUser():
    "TODO"
