import pytest, os

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

def test_singlePlatform():
    result = igdb.platforms(11)
    assert result != []
def test_multiplePlatform():
    result = igdb.platforms({
        'ids':[13,5,3]
    })
    assert result != []
