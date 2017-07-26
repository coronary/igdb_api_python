import pytest, os

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

def test_singleGameMode():
    result = igdb.game_modes(1)
    assert result != []
def test_multipleGameMode():
    result = igdb.game_modes({
        'ids':[2,3,5]
    })
    assert result != []
