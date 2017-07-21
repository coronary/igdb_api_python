from igdb import igdb
igdb = igdb()
result = igdb.getGameById(1942)
print("Retrieved: " + result["name"])
