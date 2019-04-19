from igdb import igdb
import json


file = open("key.txt", "r")
key = file.readline().strip()
gameObject = igdb(key)
result = gameObject.games({'search': "battlefield 1", 'fields' : 'name, genres'})
#result = gameObject.games(1942)

for game in result:
	search = game.decode('utf-8')
	#search.strip()
	json.loads(search)
	print("Retrieved: " + str(search))
