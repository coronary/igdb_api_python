import pytest, os

from igdb_api_python.igdb import igdb as igdb

igdb = igdb(os.environ['api_key'])

def test_singleTheme():
    result = igdb.themes(34)
    assert result != []
def test_multipleTheme():
    result = igdb.themes({
        'ids':[22,23,28]
    })
    assert result != []
