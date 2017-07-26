import pytest, os

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

def test_singleGameEngine():
    result = igdb.game_engines(67)
    assert result != []
def test_multipleGameEngine():
    result = igdb.game_engines({
        'ids':[367,363,359]
    })
    assert result != []
