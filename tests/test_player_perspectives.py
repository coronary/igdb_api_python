import pytest, os

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

def test_singlePlayerPerspective():
    result = igdb.player_perspectives(2)
    assert result != []
def test_multiplePlayerPerspective():
    result = igdb.player_perspectives({
        'ids':[7,5,4]
    })
    assert result != []
