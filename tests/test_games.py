import pytest, os

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

def test_singleGame():
    result = igdb.games(1942)
    assert result != []
def test_multipleGames():
    result = igdb.games({
        'ids':[27193,23212,1942]
    })
    assert result != []
