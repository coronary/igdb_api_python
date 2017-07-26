import pytest, os

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

def test_singleCollection():
    result = igdb.collections(1194)
    assert result != []
def test_multipleCollection():
    result = igdb.collections({
        'ids':[1198,1199,1200]
    })
    assert result != []
