from igdb import igdb

# ENTER YOUR API KEY HERE
igdb = igdb("YOUR_API_KEY")

result = igdb.getGameById(1942)
print("Retrieved: " + result["name"])
