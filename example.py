#from ig import igdb
#from igdb_api_python import igdb
from igdb_api_python.igdb import igdb as igdb
import time, os

#ENTER YOUR KEY HERE
igdb = igdb(os.environ['api_key'])

#RETRIEVE ONE GAME
result = igdb.games(1942)
for game in result:
    print("Retrieved: " + game["name"])

#Get information about ,multiple games
result = igdb.games({
    'ids':[27193,23212,1942]
})

#Get information about ,multiple games
result = igdb.pulses(25039)

#GET PLAYSTATION GAMES
result = igdb.platforms({
    'ids':42,
    'fields' : 'games'
})

#GET PLAYSTATION GAMES
result = igdb.platforms({
    'ids':42,
    'fields' : ['games','name']
})

#GET COMING SOOM PLAYSTATION 4 GAMES
result = igdb.release_dates({
    'filters' :{
        "[platform][eq]": 48,
        "[date][gt]"    : int(round(time.time() * 1000))
    },
    'order':"date:asc",
    'fields':"game"
})
# 5 game companies with name descending and offset of 5
result = igdb.companies({
    'fields': 'name',
    'limit': 5,
    'offset': 5,
    'order': 'name:desc'
})
