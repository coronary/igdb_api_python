# IGDB PYTHON WRAPPER

import requests
import json

class igdb:
    
    __api_key = ""

    def __init__(self,api_key):
        self.__api_key = api_key
        if self.__api_key == "":
            print("Please provide your key from api.igdb.com")
            exit()

    #CALL TO THE API
    def callApi(self,params):
        url = 'https://api-2445582011268.apicast.io/' + params
        headers = {
            'user-key': self.__api_key,
            'Accept' : 'application/json'
            }
        r = requests.get(url, headers=headers)
        return r

    #RETURN 1 GAME BY ID
    def getGameById(self,game_id):
        r = self.callApi("games/"+ str(game_id) +"?fields=*")
        if r.status_code == 200:
            r = json.loads(r.text)
            return r[0]
        else:
            print("Game not found")
            exit()
