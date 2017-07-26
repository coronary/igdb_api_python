import pytest, os

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

def test_singleGenre():
    result = igdb.genres(2)
    assert result != []
def test_multipleGenre():
    result = igdb.genres({
        'ids':[7,5,10]
    })
    assert result != []
