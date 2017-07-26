import pytest, os

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

def test_singleGameMode():
    result = igdb.callApi("game_modes", 25039)
    assert result.status_code == 200
def test_multipleGameMode():
    result = igdb.callApi("game_modes",{
        'ids':[25044,25042,25041]
    })
    assert result.status_code == 200
