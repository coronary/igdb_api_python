import pytest, os

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

def test_singleGame():
    result = igdb.games(1942)
def test_multipleGames():
    result = igdb.callApi("games",{
        'ids':[27193,23212,1942]
    })
    assert result.status_code == 200
