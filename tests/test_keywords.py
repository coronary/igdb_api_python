import pytest, os

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

def test_singleKeyword():
    result = igdb.keywords(1083)
    assert result != []
def test_multipleKeyword():
    result = igdb.keywords({
        'ids':[1086,1090,193]
    })
    assert result != []
