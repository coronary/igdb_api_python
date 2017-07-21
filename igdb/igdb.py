# IGDB PYTHON WRAPPER

import requests

class igdb:
    __api_key = "8bdbeba36569ad2f259749bc031e2924"
    def callApi(params):
        call_time = time.time()
        url = 'https://api-2445582011268.apicast.io/' + params
        headers = {
            #af95de8b0f345cf9fb3c141e5c874546 sharp
            #8bdbeba36569ad2f259749bc031e2924 igdb
            'user-key': api_key,
            'Accept' : 'application/json'
            }
        r = requests.get(url, headers=headers)
        print("API: %s seconds ---" % (time.time() - call_time))
        return r
    def test():
        print("test")
