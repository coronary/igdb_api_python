import pytest, os

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

def test_singleCharacter():
    result = igdb.characters(8529)
    assert result != []
def test_multipleCharacter():
    result = igdb.characters({
        'ids':[8530,8531,8533]
    })
    assert result != []
