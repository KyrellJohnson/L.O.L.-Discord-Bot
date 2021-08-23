from riotAPI_Handler import *
from databaseHandler import *

def readCommand(command, user, DB_Client):
    
    #!rank command
    if(command.startswith("!rank")):
        return(initRankCommand(command))
    elif(command.startswith("!profile")):
        return(initProfileCommand(command, user, DB_Client))

def initRankCommand(msg):

    if(msg != '!rank'):
        #strip out !rank
        returnMSG = msg.lstrip('!rank')
        #remove leading whitespace
        returnMSG = returnMSG.lstrip()
        
        #Get rank of player specified
        #Call Riot API to get player rank
        rank = findRank(returnMSG, 'na1')
       
        #send discord message
        return rank
    elif(msg == '!rank'):
        #TODO: Access Database to see if that discord user has associated Summoner Name
        #TODO: IF user_found THEN display their rank
        # .. If not found tell user their name isnt assigned to a summoner name
        # .. Or they are unranked
        return 'ERROR'

def initProfileCommand(msg, user, DB_Client):

    #set user as string
    user = str(user)

    if(msg.startswith("!profile -set")):
        #strip out command text
        returnMSG = msg.lstrip("!profile -set")
        #add account to database
        return addSummonerToUser(returnMSG, user, DB_Client)


    